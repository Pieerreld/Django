from django import forms
from django.core.exceptions import ValidationError
from project.models import Machine 
from project.models import Personnel

class AddMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=Machine.TYPE)
    personnel = forms.ModelChoiceField(queryset=Personnel.objects.all(), label='Personnel', to_field_name='id')
    etat = forms.ChoiceField(choices=Machine.ETAT)
    ip = forms.GenericIPAddressField(label='Adresse IP')

    def clean_nom(self):
        data = self.cleaned_data['nom']
        return data

    def clean_mach(self):
        data = self.cleaned_data['mach']
        return data
    
    def clean_personnel(self):
        data = self.cleaned_data['personnel']
        return data
    
    def clean_etat(self):
        data = self.cleaned_data['etat']
        return data
    
    def cleaned_ip(self):
        data = self.cleaned_data["ip"]
        return data

class AddPersonnelForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom du personnel')
    prenom = forms.CharField(required=True, label='Prénom du personnel')
    poste = forms.ChoiceField(choices=Personnel.POSTE)
    etat = forms.ChoiceField(choices=Personnel.ETAT)

    def clean_nom(self):
        data = self.cleaned_data['nom']
        return data

    def clean_prenom(self):
        data = self.cleaned_data['prenom']
        return data

    def clean_poste(self):
        data = self.cleaned_data['poste']
        return data

    def clean_etat(self):
        data = self.cleaned_data['etat']
        return data
    
class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['personnel', 'etat', 'ip', 'maintenanceDate']

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['poste', 'etat']