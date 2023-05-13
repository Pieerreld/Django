from django.shortcuts import render
from project.models import Personnel

def index(request) :

    personnels = Personnel.objects.all()

    context = {
        'personnels' : personnels,
    }
    return render(request, 'templates/index.html', context)

