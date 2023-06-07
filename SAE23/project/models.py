from datetime import datetime, date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Modèle pour représenter les infrastructures
class Infrastructure(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=30)
    lieu = models.CharField(max_length=30)
    reseau = models.GenericIPAddressField(default='0.0.0.0')

    def __str__(self):
        return f"{self.nom} {self.lieu}"

# Modèle pour représenter le personnel
class Personnel(models.Model):
    POSTE =(
        ('Technicien', ("Technicien - S'occupe de la maintenance")),
        ('Manager', ('Manager - Dirige une équipe de techniciens')),
        ('Employee', ('Employee - Travaille sur PC/Mac au bureau')),
        ('Administrator', ('Administrator - Installe et maintient le réseau'))
    )

    ETAT = (
        ('connecte', ('Utilisateur en ligne')),
        ('hors ligne', ('Utilisateur hors ligne')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=15)
    poste = models.CharField(max_length=32, choices=POSTE, default='Employee')
    etat = models.CharField(max_length=16, choices=ETAT, default='connecte')
    lieu = models.ForeignKey(Infrastructure, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Modèle pour représenter les machines
class Machine(models.Model):
    TYPE = (
       ('PC', ('PC - Utilise Windows')),
       ('Mac', ('Mac - Utilise MacOS')),
       ('Serveur', ('Serveur - Héberge des services (web, ftp)')),
       ('Switch', ('Switch - Permet la connexion et la gestion des serveurs')),
   )
    
    ETAT = (
        ('en ligne', ('Machine en ligne')),
        ('hors ligne', ('Machine hors ligne')),
        ('maintenance', ('Machine en cours de redémarrage')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=40)
    maintenanceDate = models.DateField(default=date.today)
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_DEFAULT, default=1)
    etat = models.CharField(max_length=16, choices=ETAT, default='en ligne')
    ip = models.GenericIPAddressField(default='0.0.0.0')
