from django.urls import path
from . import views

urlpatterns = [
    path('farms/', views.FarmListView.as_view(), name='farm-list'),
    path('farms/new/', views.FarmCreateView.as_view(), name='farm-create'),
    path('farms/<int:pk>/', views.FarmDetailView.as_view(), name='farm-detail'),
    path('farms/<int:pk>/edit/', views.FarmUpdateView.as_view(), name='farm-update'),
    path('crops/', views.CropListView.as_view(), name='crop-list'),
] 