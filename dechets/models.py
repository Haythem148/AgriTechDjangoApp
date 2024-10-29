from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from farms.models import Farm  # Ajustez le chemin d'importation selon votre structure

# Create your models here.

class TypeDechet(models.Model):
    METHODE_CHOICES = [
        ('COMPOST', 'Compostage'),
        ('RECYCLAGE', 'Recyclage'),
        ('INCINERATION', 'Incinération'),
        ('ENFOUISSEMENT', 'Enfouissement'),
    ]

    nom = models.CharField(max_length=100)
    description = models.TextField()
    biodegradable = models.BooleanField(default=True)
    methode_traitement = models.CharField(
        max_length=20,
        choices=METHODE_CHOICES,
        default='COMPOST'
    )
    efficacite_traitement = models.IntegerField(
        default=75,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = "Type de déchet"
        verbose_name_plural = "Types de déchets"

    def __str__(self):
        return self.nom

class PlanGestionDechets(models.Model):
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        verbose_name="Exploitation agricole"
    )
    type_dechet = models.ForeignKey(
        TypeDechet,
        on_delete=models.CASCADE,
        verbose_name="Type de déchet"
    )
    quantite = models.FloatField(verbose_name="Quantité (kg)")
    date = models.DateField(verbose_name="Date de génération")

    class Meta:
        verbose_name = "Plan de gestion des déchets"
        verbose_name_plural = "Plans de gestion des déchets"

    def __str__(self):
        return f"Plan {self.farm} - {self.type_dechet} - {self.date}"
