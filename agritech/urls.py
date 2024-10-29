from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farms.urls')),  # Remove 'api/' if it's there
    path('', include('farms.urls_frontend')),  # HTML views
]
