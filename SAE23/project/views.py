from django.shortcuts import redirect, render
from project.models import Personnel
from project.models import Machine
from django.shortcuts import get_object_or_404
from .forms import AddMachineForm
from .forms import AddPersonnelForm

def index(request) :
    
    return render(request, 'templates/index.html')


def liste_personnel(request) :
    personnels = Personnel.objects.all()

    context = {
        'personnels' : personnels,
    }
    return render(request, 'templates/liste_personnel.html', context)

def liste_machine(request) :
    machines = Machine.objects.all()

    context = {
        'machines' : machines,
    }
    return render(request, 'templates/liste_machine.html', context)

def machine_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render (request,
            'templates/machine_view.html', context)

def personnel_view(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    context={'personnel': personnel}
    return render (request,
            'templates/personnel_view.html', context)

def supprimer_machine(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    if request.method =='POST':
        machine.delete()
        return redirect('liste_machine')
    return render(request, 'templates/supprimer_machine.html', {'machine': machine})

def supprimer_personnel(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    if request.method =='POST':
        personnel.delete()
        return redirect('liste_personnel')
    return render(request, 'templates/supprimer_personnel.html', {'personnel': personnel})

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'], mach=form.cleaned_data['mach'], etat=form.cleaned_data['etat'])
            new_machine.save()
            return redirect('liste_machine') 
    else:
        form = AddMachineForm()
    context = {'form': form}
    return render(request, 'templates/add.html', context)

def personnel_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personnel = Personnel(nomm=form.cleaned_data['nom'], prenom=form.cleaned_data['prenom'], poste=form.cleaned_data['poste'], etatt=form.cleaned_data['etatt'])
            new_personnel.save()
            return redirect('liste_personnel') 
    else:
        form = AddPersonnelForm()
    context = {'form': form}
    return render(request, 'templates/add.html', context)