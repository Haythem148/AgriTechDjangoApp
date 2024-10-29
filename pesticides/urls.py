from django.urls import path
from . import views

app_name = 'pesticides'

urlpatterns = [
    # Pesticide URLs
    path('', views.PesticideListView.as_view(), name='pesticide-list'),
    path('create/', views.PesticideCreateView.as_view(), name='pesticide-create'),
    path('<int:pk>/', views.PesticideDetailView.as_view(), name='pesticide-detail'),
    path('<int:pk>/update/', views.PesticideUpdateView.as_view(), name='pesticide-update'),
    path('<int:pk>/delete/', views.PesticideDeleteView.as_view(), name='pesticide-delete'),
    
    # Application URLs
    path('applications/', views.ApplicationListView.as_view(), name='application-list'),
    path('applications/create/', views.ApplicationCreateView.as_view(), name='application-create'),
    path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='application-update'),
    path('applications/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application-delete'),
] 