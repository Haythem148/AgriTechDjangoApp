from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pesticides/', include('pesticides.urls', namespace='pesticides')),

    path('dechets/', include('dechets.urls', namespace='dechets')),
    path('farms/', include('farms.urls')),
] 