# water_management/admin.py
from django.contrib import admin
from .models import SourceEau, UtilisationEau

admin.site.register(SourceEau)
admin.site.register(UtilisationEau)
