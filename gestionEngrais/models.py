from django.db import models

class Engrais(models.Model):
    nom = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    recommandation_dose = models.FloatField()
    type_sol = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class ApplicationEngrais(models.Model):
    engrais = models.ForeignKey(Engrais, on_delete=models.CASCADE)
    date = models.DateField()
    quantite = models.FloatField()
    ia = models.TextField()  # Optimisation details

    def __str__(self):
        return f"{self.engrais.nom} applied on {self.date}"
