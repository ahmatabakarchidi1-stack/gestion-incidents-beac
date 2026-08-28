from django.contrib import admin
from .models import Categorie, Incident, Profil

# Register your models here.

admin.site.register(Categorie)
admin.site.register(Incident)
admin.site.register(Profil)