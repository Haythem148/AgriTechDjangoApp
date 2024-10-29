# farmer/forms.py
from django import forms
from .models import Agriculteur
from django.contrib.auth.forms import UserCreationForm

class AgriculteurCreationForm(UserCreationForm):
    class Meta:
        model = Agriculteur
        fields = ['username', 'cin', 'email', 'password1', 'password2']
