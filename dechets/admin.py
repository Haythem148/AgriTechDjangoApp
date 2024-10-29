from django.contrib import admin
from .models import TypeDechet, PlanGestionDechets

@admin.register(TypeDechet)
class TypeDechetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'biodegradable', 'methode_traitement')
    list_filter = ('biodegradable',)
    search_fields = ('nom', 'methode_traitement')

@admin.register(PlanGestionDechets)
class PlanGestionDechetsAdmin(admin.ModelAdmin):
    list_display = ('farm', 'type_dechet', 'quantite', 'date')
    list_filter = ('type_dechet', 'date')
    search_fields = ('farm__name', 'type_dechet__nom')  # Supposant que Farm a un champ 'name'
    date_hierarchy = 'date'
