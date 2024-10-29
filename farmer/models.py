# farmer/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

def verif_cin(value):
    if len(str(value)) != 8:
        raise ValidationError("Votre CIN doit comporter exactement 8 chiffres.")
    return value

class Agriculteur(AbstractUser):
    cin = models.IntegerField(validators=[verif_cin], unique=True)
    email = models.EmailField(unique=True)
