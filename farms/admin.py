from django.contrib import admin
from .models import Farm, Crop

@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('name', 'farm', 'crop_type', 'area', 'planting_date', 'expected_harvest_date')
    list_filter = ('crop_type', 'farm')
    search_fields = ('name', 'farm__name')
    date_hierarchy = 'planting_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'farm', 'crop_type', 'area')
        }),
        ('Dates', {
            'fields': ('planting_date', 'expected_harvest_date')
        }),
        ('Additional Information', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'area')
    search_fields = ('name', 'location')
