from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from incidents.views import health_check, predire_categorie


def accueil(request):
    return JsonResponse({
        "message": "GestionIncidentsBEAC API",
        "status": "ok"
    })


urlpatterns = [
    path('', accueil),
    path('admin/', admin.site.urls),
    path('api/', include('incidents.urls')),
    path('health/', health_check),
    path('api/predict/', predire_categorie),
]