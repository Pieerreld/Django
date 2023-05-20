from django.shortcuts import render
from project.models import Personnel
from project.models import Machine
from django.shortcuts import get_object_or_404

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