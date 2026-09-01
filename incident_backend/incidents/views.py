from rest_framework import viewsets
from .models import Categorie, Incident, Profil
from .serializers import CategorieSerializer, IncidentSerializer, ProfilSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class ProfilViewSet(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer

from django.http import JsonResponse
from django.db import connection

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        db_status = "ok"
    except Exception:
        db_status = "erreur"

    return JsonResponse({
        "serveur": "ok",
        "base_de_donnees": db_status,
    })

import joblib
import os

# Charger le modèle une seule fois au démarrage du serveur
CHEMIN_MODELE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ia', 'modele_categorie.pkl')
try:
    modele_ia = joblib.load(CHEMIN_MODELE)
except FileNotFoundError:
    modele_ia = None

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def predire_categorie(request):
    if modele_ia is None:
        return Response({"erreur": "Modèle IA non disponible"}, status=500)

    texte = request.data.get('description', '')
    if not texte:
        return Response({"erreur": "Le champ 'description' est requis"}, status=400)

    prediction = modele_ia.predict([texte])[0]
    return Response({"categorie_predite": prediction})