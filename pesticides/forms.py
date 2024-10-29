from django import forms
from .models import Pesticide, Application

class PesticideForm(forms.ModelForm):
    class Meta:
        model = Pesticide
        fields = ['nom', 'type_pesticide', 'composition', 'type_culture', 'dose_recommandee', 'delai_reentree']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du pesticide'
            }),
            'type_pesticide': forms.Select(attrs={
                'class': 'form-control'
            }),
            'composition': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Composition chimique'
            }),
            'type_culture': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dose_recommandee': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': '0.1',
                'placeholder': 'L/ha'
            }),
            'delai_reentree': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': 'Heures'
            })
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['farm', 'pesticide', 'date_application', 'quantite']
        widgets = {
            'farm': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Sélectionner une exploitation'
            }),
            'pesticide': forms.Select(attrs={
                'class': 'form-select',
                'placeholder': 'Sélectionner un pesticide'
            }),
            'date_application': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.1'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        pesticide = cleaned_data.get('pesticide')
        quantite = cleaned_data.get('quantite')
        
        if quantite and quantite <= 0:
            self.add_error('quantite', 'La quantité doit être supérieure à 0')
        
        return cleaned_data