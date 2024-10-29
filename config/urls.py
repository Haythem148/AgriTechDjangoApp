from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dechets/', include('dechets.urls', namespace='dechets')),
    path('farms/', include('farms.urls')),
] 