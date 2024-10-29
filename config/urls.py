from django.urls import path, include

urlpatterns = [
    path('farms/', include('farms.urls')),
] 