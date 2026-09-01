from rest_framework import serializers
from .models import Categorie, Incident, Profil, Commentaire

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'


class CommentaireSerializer(serializers.ModelSerializer):
    auteur_nom = serializers.CharField(source='auteur.username', read_only=True)

    class Meta:
        model = Commentaire
        fields = ['id', 'incident', 'auteur', 'auteur_nom', 'message', 'date_creation']