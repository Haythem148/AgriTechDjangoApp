from django.urls import path
from .views import (
    engrais_list, engrais_create, engrais_update, engrais_delete,
    application_engrais_list, application_engrais_create
)

urlpatterns = [
    path('', engrais_list, name='engrais-list'),
    path('add/', engrais_create, name='engrais-create'),
    path('edit/<int:pk>/', engrais_update, name='engrais-update'),
    path('delete/<int:pk>/', engrais_delete, name='engrais-delete'),
    path('applications/', application_engrais_list, name='application-engrais-list'),
    path('applications/add/', application_engrais_create, name='application-engrais-create'),
]
