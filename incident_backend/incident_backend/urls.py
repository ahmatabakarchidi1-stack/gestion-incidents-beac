from django.contrib import admin
from django.urls import path, include
from incidents.views import health_check, predire_categorie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('incidents.urls')),
    path('health/', health_check),
    path('api/predict/', predire_categorie),
]