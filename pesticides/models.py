from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from farms.models import Farm

# Create your models here.

class Pesticide(models.Model):
    TYPE_CHOICES = [
        ('herbicide', 'Herbicide'),
        ('insecticide', 'Insecticide'),
        ('fongicide', 'Fongicide'),
        ('autre', 'Autre'),
    ]

    CULTURE_CHOICES = [
        ('CEREALES', 'Céréales'),
        ('LEGUMES', 'Légumes'),
        ('FRUITS', 'Fruits'),
        ('VIGNE', 'Vigne'),
        ('AUTRE', 'Autre'),
    ]

    nom = models.CharField(max_length=100, verbose_name="Nom")
    composition = models.TextField(verbose_name="Composition chimique")
    type_pesticide = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name="Type de pesticide"
    )
    type_culture = models.CharField(
        max_length=20,
        choices=CULTURE_CHOICES,
        default='AUTRE',
        verbose_name="Type de culture"
    )
    dose_recommandee = models.FloatField(
        verbose_name="Dose recommandée (L/ha)",
        validators=[MinValueValidator(0)]
    )
    delai_reentree = models.IntegerField(
        verbose_name="Délai de réentrée (heures)",
        validators=[MinValueValidator(0)],
        help_text="Délai minimum avant de pouvoir retourner sur la parcelle"
    )

    class Meta:
        verbose_name = "Pesticide"
        verbose_name_plural = "Pesticides"

    def __str__(self):
        return f"{self.nom} ({self.get_type_pesticide_display()})"

class Application(models.Model):
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        verbose_name="Exploitation agricole"
    )
    pesticide = models.ForeignKey(
        Pesticide,
        on_delete=models.CASCADE,
        verbose_name="Pesticide"
    )
    quantite = models.FloatField(
        verbose_name="Quantité (L)",
        validators=[MinValueValidator(0)]
    )
    date_application = models.DateField(verbose_name="Date d'application")
    conditions_meteo = models.TextField(
        verbose_name="Conditions météorologiques",
        blank=True,
        help_text="Température, vent, humidité..."
    )

    class Meta:
        verbose_name = "Application de pesticide"
        verbose_name_plural = "Applications de pesticides"
        ordering = ['-date_application']

    def __str__(self):
        return f"Application de {self.pesticide} sur {self.farm} le {self.date_application}"
