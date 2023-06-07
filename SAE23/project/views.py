from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from project.models import Personnel
from project.models import Machine
from project.models import Infrastructure
from django.shortcuts import get_object_or_404
from .forms import AddMachineForm
from .forms import AddPersonnelForm
from django.contrib.auth.decorators import user_passes_test
from .forms import MachineForm
from .forms import PersonnelForm
from django.db.models import Q



def index(request) :
    
    return render(request, 'templates/index.html')

def specific_user_check(user):
    return user.username == 'admin'

def login(request) :
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                next_page = request.POST.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('homepage')
            else:
                error_message = 'Identifiant ou mot de passe incorrect.'
                return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@login_required
def profile(request):
    user = request.user
    return render(request, 'templates/profile.html', {'user': user})

def logout(request):
  auth_logout(request)
  return redirect('index')

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

@user_passes_test(specific_user_check)
def supprimer_machine(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    if request.method =='POST':
        machine.delete()
        return redirect('liste_machine')
    return render(request, 'templates/supprimer_machine.html', {'machine': machine})

@user_passes_test(specific_user_check)
def supprimer_personnel(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    if request.method =='POST':
        personnel.delete()
        return redirect('liste_personnel')
    return render(request, 'templates/supprimer_personnel.html', {'personnel': personnel})

@user_passes_test(specific_user_check)
def add_machine_personnel(request):
    machine_form = AddMachineForm()
    personnel_form = AddPersonnelForm()
    if request.method == 'POST':
        if 'machine_submit' in request.POST:
            machine_form = AddMachineForm(request.POST)
            if machine_form.is_valid():
                new_machine = Machine(nom=machine_form.cleaned_data['nom'], mach=machine_form.cleaned_data['mach'], etat=machine_form.cleaned_data['etat'], ip=machine_form.cleaned_data['ip'],)
                new_machine.save()
                return redirect('liste_machine')

        if 'personnel_submit' in request.POST:
            personnel_form = AddPersonnelForm(request.POST)
            if personnel_form.is_valid():
                new_personnel = Personnel(nom=personnel_form.cleaned_data['nom'], prenom=personnel_form.cleaned_data['prenom'], poste=personnel_form.cleaned_data['poste'], etat=personnel_form.cleaned_data['etat'])
                new_personnel.save()
                return redirect('liste_personnel')
    else:
        machine_form = AddMachineForm()
        personnel_form = AddPersonnelForm()

    return render(request, 'templates/ajout_machine_personnel.html', {
        'machine_form': machine_form,
        'personnel_form': personnel_form,
    })

def chatbot(request) :
    machines = Machine.objects.all()
    context = {'machines': machines}
    return render(request, 'templates/chatbot.html')

@user_passes_test(specific_user_check)
def edit_machine(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect('liste_machine')
    else:
        form = MachineForm(instance=machine)

    return render(request, 'edit_machine.html', {'form': form})

@user_passes_test(specific_user_check)
def edit_personnel(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('liste_personnel')
    else:
        form = PersonnelForm(instance=personnel)

    return render(request, 'edit_personnel.html', {'form': form})

def recherche(request):
    query = request.GET.get('q')
    personnels = Personnel.objects.filter(
        Q(nom__icontains=query) |
        Q(prenom__icontains=query) | 
        Q(poste__icontains=query) |
        Q(etat__icontains=query) |
        Q(lieu__lieu__icontains=query) 
    )
    machines = Machine.objects.filter(
        Q(nom__icontains=query) |
        Q(mach__icontains=query) |
        Q(personnel__nom__icontains=query) |
        Q(etat__icontains=query) |
        Q(ip__icontains=query) 
    )
    infrastructures = Infrastructure.objects.filter(
        Q(nom__icontains=query) |
        Q(lieu__icontains=query) |
        Q(reseau__icontains=query) 
    )

    fields_personnel = [
    {'name': field.name, 'verbose_name': field.verbose_name, 'value': getattr(Personnel, field.name)}
    for field in Personnel._meta.get_fields()
    if not field.is_relation
]
    fields_machine = [field for field in Machine._meta.get_fields() if field.concrete]
    fields_infra = [field for field in Infrastructure._meta.get_fields() if field.concrete]
    
    context = {
        'personnels': personnels,
        'machines': machines,
        'infrastructures' : infrastructures,
        'fields_personnel': fields_personnel,
        'fields_machine': fields_machine,
        'fields_infra': fields_infra,
        'query': query
    }
    return render(request, 'recherche.html', context)