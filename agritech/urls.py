from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farms.urls')),  # Remove 'api/' if it's there
    path('', include('farms.urls_frontend')), 
    path('dechets/', include('dechets.urls', namespace='dechets')),
    path('pesticides/', include('pesticides.urls', namespace='pesticides')), # HTML views
    path('engrais/', include('gestionEngrais.urls')),


]
