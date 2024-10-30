from django import forms
from .models import Engrais,ApplicationEngrais
from huggingface_hub import InferenceClient
import requests
import re

class EngraisForm(forms.ModelForm):
    class Meta:
        model = Engrais
        fields = ['nom', 'composition', 'type_sol']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'composition': forms.TextInput(attrs={'class': 'form-control'}),
            'type_sol': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def get_ia_recommendation(self, nom, composition, type_sol):
        try:
            GROQ_API_KEY = "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"
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            
            prompt = f"""En tant qu'expert en agronomie, analysez ces informations:
            Nom de l'engrais: {nom}
            Composition: {composition}
            Type de sol: {type_sol}
            
            Donnez uniquement la dose recommandée en kg/ha sous forme d'un nombre, sans texte supplémentaire."""
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json={
                    "model": "mixtral-8x7b-32768",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.1,
                    "max_tokens": 10
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                text_response = result['choices'][0]['message']['content']
                numbers = re.findall(r'\d+(?:\.\d+)?', text_response)
                if numbers:
                    return float(numbers[0])
                    
            return self.calculate_fallback_dose(composition, type_sol)
                
        except Exception as e:
            print(f"Erreur API Groq: {str(e)}")
            return self.calculate_fallback_dose(composition, type_sol)

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Calculer la dose recommandée avant la sauvegarde
        try:
            dose = self.get_ia_recommendation(
                instance.nom,
                instance.composition,
                instance.type_sol
            )
            instance.recommandation_dose = dose
        except Exception as e:
            instance.recommandation_dose = self.calculate_fallback_dose(
                instance.composition,
                instance.type_sol
            )
            
        if commit:
            instance.save()
        return instance

    def calculate_fallback_dose(self, composition, type_sol):
        """Méthode de secours si l'API échoue"""
        base_dose = 100.0
        
        composition = composition.lower()
        if "azote" in composition or "n" in composition:
            base_dose *= 1.2
        if "phosphore" in composition or "p" in composition:
            base_dose *= 1.1
        
        type_sol = type_sol.lower()
        if "argileux" in type_sol:
            base_dose *= 0.9
        elif "sableux" in type_sol:
            base_dose *= 1.1
            
        return round(base_dose, 2)

    def clean_composition(self):
        composition = self.cleaned_data.get('composition')
        if not any(x in composition.lower() for x in ['n-p-k', 'azote', 'phosphore', 'potassium']):
            raise forms.ValidationError("La composition doit contenir au moins un des éléments N-P-K, Azote, Phosphore ou Potassium")
        return composition

    def clean_type_sol(self):
        type_sol = self.cleaned_data.get('type_sol')
        if not any(x in type_sol.lower() for x in ['argileux', 'sableux', 'limoneux']):
            raise forms.ValidationError("Le type de sol doit être Argileux, Sableux ou Limoneux")
        return type_sol

class ApplicationEngraisForm(forms.ModelForm):
    class Meta:
        model = ApplicationEngrais
        fields = ['engrais', 'date', 'quantite', 'ia']
        widgets = {
            'engrais': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.1'
            }),
            'ia': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notes sur l\'optimisation IA...'
            })
        }

    def clean_quantite(self):
        quantite = self.cleaned_data.get('quantite')
        if quantite and quantite < 0:
            raise forms.ValidationError("La quantité ne peut pas être négative.")
        return quantite