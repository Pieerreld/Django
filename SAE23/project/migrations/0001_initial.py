# Generated by Django 4.2.1 on 2023-05-12 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=6)),
                ('maintenanceDate', models.DateField(default=datetime.datetime(2023, 5, 12, 22, 27, 4, 487565, tzinfo=datetime.timezone.utc))),
                ('mach', models.CharField(choices=[('PC', 'PC - Run windows'), ('Mac', 'MAc - Run MacOS'), ('Serveur', 'Serveur - Simple Server to deploy virtual machines'), ('Switch', 'Switch - To maintains and connect servers')], default='PC', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=15)),
                ('poste', models.CharField(choices=[('Technicien', 'Technicien - Takes care of the maintenance'), ('Manager', 'Manager - Lead a team of Technicien'), ('Employee', 'Employee - Work on the PC/Mac at the office')], default='Employee', max_length=32)),
            ],
        ),
    ]
