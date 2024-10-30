from django import forms
from .models import TypeDechet, PlanGestionDechets

class TypeDechetForm(forms.ModelForm):
    class Meta:
        model = TypeDechet
        fields = ['nom', 'description', 'biodegradable', 'methode_traitement', 'efficacite_traitement']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control'
            }),
            'efficacite_traitement': forms.NumberInput(attrs={
                'min': 0, 
                'max': 100,
                'class': 'form-control'
            }),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'methode_traitement': forms.Select(attrs={'class': 'form-control'}),
            'biodegradable': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class PlanGestionDechetsForm(forms.ModelForm):
    class Meta:
        model = PlanGestionDechets
        fields = ['farm', 'type_dechet', 'quantite', 'date']
        widgets = {
            'farm': forms.Select(attrs={'class': 'form-control'}),
            'type_dechet': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'quantite': forms.NumberInput(attrs={
                'min': 0,
                'step': '0.01',
                'class': 'form-control'
            })
        } 