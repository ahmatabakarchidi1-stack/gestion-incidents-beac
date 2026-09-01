import os
import django
import sys

# Permet au script d'accéder à Django et sa base de données
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'incident_backend.settings')
django.setup()

from incidents.models import Incident
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

# 1. Récupérer les incidents depuis la base de données
incidents = Incident.objects.select_related('categorie').all()

textes = []
categories = []

for incident in incidents:
    if incident.categorie:
        # On combine titre + description pour plus de contexte
        texte = f"{incident.titre} {incident.description}"
        textes.append(texte)
        categories.append(incident.categorie.nom)

print(f"Nombre d'incidents utilisés pour l'entraînement : {len(textes)}")

if len(textes) < 5:
    print("Pas assez de données pour entraîner le modèle (minimum 5 incidents recommandé).")
else:
    # 2. Créer le pipeline : transformation texte -> vecteurs + classificateur
    modele = make_pipeline(TfidfVectorizer(), MultinomialNB())

    # 3. Entraîner le modèle
    modele.fit(textes, categories)

    # 4. Sauvegarder le modèle entraîné dans un fichier
    chemin_modele = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modele_categorie.pkl')
    joblib.dump(modele, chemin_modele)

    print(f"Modèle entraîné et sauvegardé avec succès : {chemin_modele}")

    # Test rapide
    test_texte = ["Le réseau ne fonctionne plus depuis ce matin"]
    prediction = modele.predict(test_texte)
    print(f"Test — texte: '{test_texte[0]}' → catégorie prédite: {prediction[0]}")