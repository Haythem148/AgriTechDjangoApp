from django.core.validators import MinValueValidator
from django.db import models

class Engrais(models.Model):
    nom = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    recommandation_dose = models.FloatField(validators=[MinValueValidator(0.0)])
    type_sol = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Engrais"
        verbose_name_plural = "Engrais"

    def __str__(self):
        return self.nom

    def get_total_applications(self):
        return self.applicationengrais_set.count()

class ApplicationEngrais(models.Model):
    engrais = models.ForeignKey(Engrais, on_delete=models.CASCADE)
    date = models.DateField()
    quantite = models.FloatField(validators=[MinValueValidator(0.0)])
    ia = models.TextField(verbose_name="AI Optimization")

    class Meta:
        verbose_name = "Application d'engrais"
        verbose_name_plural = "Applications d'engrais"
        ordering = ['-date']

    def __str__(self):
        return f"{self.engrais.nom} applied on {self.date}"

    engrais = models.ForeignKey(Engrais, on_delete=models.CASCADE)
    date = models.DateField()
    quantite = models.FloatField(validators=[MinValueValidator(0.0)])
    ia = models.TextField(verbose_name="AI Optimization")

    class Meta:
        verbose_name = "Application d'engrais"
        verbose_name_plural = "Applications d'engrais"
        ordering = ['-date']

    def __str__(self):
        return f"{self.engrais.nom} applied on {self.date}"