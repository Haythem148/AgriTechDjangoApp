from django.contrib import admin
from django.urls import path, include

urlpatterns = [
 path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('farms/', include('farms.urls')),
    path('engrais/', include('gestionEngrais.urls')),
    path('pesticides/', include('pesticides.urls')),
    path('dechets/', include('dechets.urls')),
    path('water-management/', include('water_management.urls')),


]
