from rest_framework import serializers
from .models import Categorie, Incident, Profil

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