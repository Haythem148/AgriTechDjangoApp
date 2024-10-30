from django.urls import path
from . import views

app_name = 'dechets'

urlpatterns = [
    path('', views.TypeDechetListView.as_view(), name='type-dechet-list'),
    path('<int:pk>/', views.TypeDechetDetailView.as_view(), name='type-dechet-detail'),
    path('create/', views.TypeDechetCreateView.as_view(), name='type-dechet-create'),
    path('<int:pk>/update/', views.TypeDechetUpdateView.as_view(), name='type-dechet-update'),
    path('<int:pk>/delete/', views.TypeDechetDeleteView.as_view(), name='type-dechet-delete'),
    path('plans/', views.PlanGestionDechetsListView.as_view(), name='plan-list'),
    path('plans/<int:pk>/', views.PlanGestionDechetsDetailView.as_view(), name='plan-detail'),
    path('plans/create/', views.PlanGestionDechetsCreateView.as_view(), name='plan-create'),
    path('plans/<int:pk>/update/', views.PlanGestionDechetsUpdateView.as_view(), name='plan-update'),
    path('plans/<int:pk>/delete/', views.PlanGestionDechetsDeleteView.as_view(), name='plan-delete'),
] 