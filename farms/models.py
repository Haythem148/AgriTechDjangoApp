from django.db import models
from django.urls import reverse

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

class Crop(models.Model):
    CROP_TYPES = [
        ('VEGETABLE', 'Vegetable'),
        ('FRUIT', 'Fruit'),
        ('GRAIN', 'Grain'),
        ('OTHER', 'Other'),
    ]

    GROWTH_STAGES = [
        ('SEEDLING', 'Seedling'),
        ('VEGETATIVE', 'Vegetative'),
        ('FLOWERING', 'Flowering'),
        ('FRUITING', 'Fruiting'),
        ('MATURE', 'Mature'),
    ]

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, related_name='crops')
    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=20, choices=CROP_TYPES)
    growth_stage = models.CharField(max_length=20, choices=GROWTH_STAGES, default='SEEDLING')
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in hectares")
    water_requirements = models.DecimalField(max_digits=10, decimal_places=2, help_text="Water needed in L/day")
    fertilizer_requirements = models.DecimalField(max_digits=10, decimal_places=2, help_text="Fertilizer needed in kg/ha")
    planting_date = models.DateField()
    expected_harvest_date = models.DateField()
    health = models.IntegerField(default=100, help_text="Crop health percentage")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} at {self.farm.name}"

    def get_absolute_url(self):
        return reverse('farms:crop-detail', kwargs={'pk': self.pk})
