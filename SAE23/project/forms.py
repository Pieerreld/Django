from django import forms
from django.core.exceptions import ValidationError
from project.models import Machine 

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


    