from django import forms
from .models import Engrais, ApplicationEngrais

class EngraisForm(forms.ModelForm):
    class Meta:
        model = Engrais
        fields = ['nom', 'composition', 'recommandation_dose', 'type_sol']

class ApplicationEngraisForm(forms.ModelForm):
    class Meta:
        model = ApplicationEngrais
        fields = ['engrais', 'date', 'quantite', 'ia']
