from django.urls import path
from .views import (
    EngraisListView, EngraisCreateView, EngraisUpdateView, EngraisDeleteView,
    ApplicationEngraisListView, ApplicationEngraisCreateView, ApplicationEngraisUpdateView, ApplicationEngraisDeleteView
)

app_name = 'gestionEngrais'

urlpatterns = [
    path('engrais/', EngraisListView.as_view(), name='engrais-list'),
    path('engrais/create/', EngraisCreateView.as_view(), name='engrais-create'),
    path('engrais/delete/<int:pk>/', EngraisDeleteView.as_view(), name='engrais-delete'),
    path('engrais/edit/<int:pk>/', EngraisUpdateView.as_view(), name='engrais-update'),
    path('applications/', ApplicationEngraisListView.as_view(), name='application-list'),
    path('applications/create/', ApplicationEngraisCreateView.as_view(), name='application-create'),
    path('applications/edit/<int:pk>/', ApplicationEngraisUpdateView.as_view(), name='application-update'),
    path('applications/delete/<int:pk>/', ApplicationEngraisDeleteView.as_view(), name='application-delete'),
]
