from datetime import datetime
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

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=15)
    poste = models.CharField(max_length=32, choices=POSTE, default='Employee')

    
class Machine(models.Model):

    TYPE = (
       ('PC', ('PC - Run windows')),
       ('Mac', ('MAc - Run MacOS')),
       ('Serveur', ('Serveur - Run some services (web,ftp)')),
       ('Switch', ('Switch - To maintains and connect servers')),
   )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=40)
    maintenanceDate = models.DateField()
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    personnel = models.ForeignKey(Personnel, on_delete=models.SET_DEFAULT, default=0)