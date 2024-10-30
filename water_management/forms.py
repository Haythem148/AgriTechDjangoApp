from django import forms
from .models import SourceEau, UtilisationEau

class SourceEauForm(forms.ModelForm):
    class Meta:
        model = SourceEau
        fields = ['nom', 'type', 'capacite', 'debit']

class UtilisationEauForm(forms.ModelForm):
    class Meta:
        model = UtilisationEau
        fields = ['farm', 'source_eau', 'quantite_utilisee', 'date']
