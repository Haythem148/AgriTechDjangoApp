from django.urls import path
from . import views

app_name = 'farms'

urlpatterns = [
    

    # Farm URLs
    path('', views.FarmListView.as_view(), name='farm-list'),
    path('farms/<int:pk>/', views.FarmDetailView.as_view(), name='farm-detail'),
    path('farms/create/', views.FarmCreateView.as_view(), name='farm-create'),
    path('farms/<int:pk>/update/', views.FarmUpdateView.as_view(), name='farm-update'),
    path('farms/<int:pk>/delete/', views.FarmDeleteView.as_view(), name='farm-delete'),
    
    # Crop URLs
    path('farms/<int:farm_pk>/crops/', views.CropListView.as_view(), name='crop-list'),
    path('farms/<int:farm_pk>/crops/create/', views.CropCreateView.as_view(), name='crop-create'),
    path('crops/<int:pk>/', views.CropDetailView.as_view(), name='crop-detail'),
    path('crops/<int:pk>/update/', views.CropUpdateView.as_view(), name='crop-update'),
    path('crops/<int:pk>/delete/', views.CropDeleteView.as_view(), name='crop-delete'),
    
    # Task URLs
]
