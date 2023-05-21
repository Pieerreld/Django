from django.shortcuts import redirect, render
from project.models import Personnel
from project.models import Machine
from django.shortcuts import get_object_or_404
from .forms import AddMachineForm

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
    return render(request, 'templates/machine_add.html', context)
