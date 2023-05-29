from datetime import datetime, date
from django.db import models
from django.urls import reverse

# Create your models here.


class Personnel(models.Model):

    POSTE = (
        ('Technicien', ('Technicien - Takes care of the maintenance')),
        ('Manager', ('Manager - Lead a team of Technicien')),
        ('Employee', ('Employee - Work on the PC/Mac at the office')),
        ('Administrator', ('Administrator - Install the network and maintain it'))
    )

    ETAT = (
        ('connecte', ('Utilisateur en ligne')),
        ('hors ligne', ('Utilisateur hors ligne')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=15)
    poste = models.CharField(max_length=32, choices=POSTE, default='Employee')
    etat = models.CharField(max_length= 16, choices=ETAT, default='connecte')

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    
class Machine(models.Model):

    TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('MAc - Run MacOS')),
       ('Serveur', ('Serveur - Run some services (web,ftp)')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )
    
    ETAT = (
        ('en ligne', ('machine is online')),
        ('hors ligne', ('machine is offline')),
        ('maintenance', ('machine restarting')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=40)
    maintenanceDate = models.DateField(default=date.today)
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_DEFAULT, default=1)
    etat = models.CharField(max_length=16, choices=ETAT, default='en ligne')