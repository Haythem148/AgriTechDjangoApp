# water_management/models.py
from django.db import models
from farms.models import Farm  # Import Farm model from farms app

class SourceEau(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    capacite = models.FloatField()  # in liters
    debit = models.FloatField()  # liters per minute

    def __str__(self):
        return f"{self.nom} ({self.type})"

class UtilisationEau(models.Model):
    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name='utilisations', null=True, blank=True
    )
    source_eau = models.ForeignKey('SourceEau', on_delete=models.CASCADE, related_name='usages')
    quantite_utilisee = models.FloatField()  # in liters
    date = models.DateField()


    def __str__(self):
        return f"Usage on {self.date} - {self.quantite_utilisee} L"
