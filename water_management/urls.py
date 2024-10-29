# water_management/urls.py
from django.urls import path
from .views import (
    source_list, source_create, source_update, source_delete, source_detail,
    utilisation_list, utilisation_create, utilisation_update, utilisation_delete, utilisation_detail,
    get_water_prediction, water_prediction_view
)

app_name = 'water_management'

# URLs for SourceEau CRUD
urlpatterns = [
    path('sources/', source_list, name='source_list'),
    path('sources/create/', source_create, name='source_create'),
    path('sources/update/<int:pk>/', source_update, name='source_update'),
    path('sources/delete/<int:pk>/', source_delete, name='source_delete'),
    path('sources/detail/<int:pk>/', source_detail, name='source_detail'),  # Detail view added here

    
    # URLs for UtilisationEau CRUD
    path('utilisations/', utilisation_list, name='utilisation_list'),
    path('utilisations/create/', utilisation_create, name='utilisation_create'),
    path('utilisations/update/<int:pk>/', utilisation_update, name='utilisation_update'),
    path('utilisations/delete/<int:pk>/', utilisation_delete, name='utilisation_delete'),
    path('utilisations/detail/<int:pk>/', utilisation_detail, name='utilisation_detail'),  # Detail view added here

    path('predict-water/', get_water_prediction, name='predict_water'),
    path('water-prediction/', water_prediction_view, name='water_prediction'),
]
