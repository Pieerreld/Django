from django import forms
from django.core.exceptions import ValidationError
from project.models import Machine 
from project.models import Personnel

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=Machine.TYPE)
    etat = forms.ChoiceField(choices=Machine.ETAT)

    def clean_nom(self):
        data = self.cleaned_data['nom']
        return data

    def clean_mach(self):
        data = self.cleaned_data['mach']
        return data
    
    def clean_etat(self):
        data = self.cleaned_data['etat']
        return data

class AddPersonnelForm(forms.Form):
    nomm = forms.CharField(required=True, label='Nom du personnel')
    prenom = forms.CharField(required=True, label='Prénom du personnel')
    poste = forms.ChoiceField(choices=Personnel.POSTE)
    etatt = forms.ChoiceField(choices=Personnel.ETAT)

    def clean_nomm(self):
        data = self.cleaned_data['nom']
        return data

    def clean_prenom(self):
        data = self.cleaned_data['prenom']
        return data

    def clean_poste(self):
        data = self.cleaned_data['poste']
        return data

    def clean_etatt(self):
        data = self.cleaned_data['etat']
        return data