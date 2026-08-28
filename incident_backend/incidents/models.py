from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Incident(models.Model):
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
        ('cloture', 'Clôturé'),
    ]
    GRAVITE_CHOICES = [
        ('critique', 'Critique'),
        ('elevee', 'Élevée'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    gravite = models.CharField(max_length=20, choices=GRAVITE_CHOICES, default='moyenne')
    declarant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidents_declares')
    technicien = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidents_assignes')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_maj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class Profil(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('responsable', 'Responsable'),
        ('technicien', 'Technicien'),
        ('utilisateur', 'Utilisateur'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='utilisateur')
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"