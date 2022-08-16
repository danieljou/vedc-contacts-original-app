from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from users.models import *
from users.decorators import *



@login_required
def home(request):
    context = {}
    user_id = request.user.id

    user2 = Personne.objects.get(user = request.user)
    allnum = Numero.objects.filter(utilisateur_id = user_id)
    context['allnum'] = allnum
    context['user2'] = user2
    return render(request, 'registration/profile.html',context)

def index(request):
    context = {}
    assemblee_count = Assemblee.objects.count()
    context['assemblee_count'] = assemblee_count

    return render(request, 'index.html',context)


def assemblees(request):
    context = {}
    assemblee_count = Assemblee.objects.count()
    assemblee = Assemblee.objects.all().order_by('Nom_assemblee')

    context['assemblee_count'] = assemblee_count
    context['assemblee'] = assemblee
    return render(request, 'assemblees.html',context)

def assemblee_details(request, assemblee_id):

    context = {}
    assemblee = Assemblee.objects.get(pk = assemblee_id)
    
    try:
        serviteur = User.objects.get(pk = assemblee.Encadreur.id)
    except:
        serviteur = False
    fidele = Personne.objects.filter(assemblee_id = assemblee_id ).order_by('user__last_name')
    all_programme = Programme.objects.filter(assemble = assemblee)
    try:
        allnum_serviteur = Numero.objects.filter(utilisateur = serviteur)
    except:
        allnum_serviteur = False

    context['serviteur'] = serviteur
    context['assemblee'] = assemblee
    context['fidele'] = fidele
    context['all_programme'] = all_programme
    context['allnum_serviteur'] = allnum_serviteur

    return render(request,'assamble_details.html' , context)


@login_required
@is_encadreur_required
def assemblees_management(request):
    context = {}
    connected_user = request.user
    connected_account = Personne.objects.get(user = connected_user)
    assemby = connected_account.assemblee
    assembies = Assemblee.objects.filter(Encadreur = connected_user)
    all_programme = Programme.objects.filter(assemble = assemby)

    context['assembies'] = assembies
    context['all_programme'] = all_programme
    return render(request, 'gerer_assemblée.html', context)


@login_required
@is_encadreur_required
def gerer_une_assemblee(request, assemble_id):
    context = {}

    connected_user = request.user

    connected_account = Personne.objects.get(user = connected_user)
    assembly = Assemblee.objects.get(pk = assemble_id)
    all_programme = Programme.objects.filter(assemble = assembly)

    context['assembly'] = assembly
    context['all_programme'] = all_programme
    return render(request, 'gerer_assemble_encadreur.html', context)

@login_required
@is_admin_required
def gestion_des_assemblee(request):
    context = {}
    assemblee = Assemblee.objects.all()
   
    
    context['assemblee'] = assemblee
    
    
    return render(request, 'gestion_assemblée.html', context)


@login_required
@is_admin_required
def assemnble_add(request):
    context = {}
    form = AssembleeForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            serv_id = form.cleaned_data['Encadreur']
            if(serv_id):
                encadreur = Personne.objects.get(user = serv_id)
                encadreur.is_encadreur = True
                encadreur.save()
            return redirect('gestion_des_assemblee')
    context['form'] = form
    return render(request, 'assemblee_add.html', context)

@login_required
@is_admin_required
def delete_assemble(request, assemble_id):
    
    context = {}
    assemble = Assemblee.objects.get(pk = assemble_id)
    assemble.delete()
    return redirect('gestion_des_assemblee')


@login_required
@is_encadreur_required
def coordonee_management(request,assemble_id):

    context = {}
    assemble = Assemblee.objects.get(pk = assemble_id)
    form = Assemble_cord_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            assemble.set_coordonnees(form.cleaned_data['Latitude'],form.cleaned_data['Longitude'])
            assemble.save()
        return redirect("assemblees_management")
    context['form'] = form
    return render(request,'corrdonees_add.html', context)


def assamblee_graph(request, assemble_id):

    context = {}
    assemble = Assemblee.objects.get(pk = assemble_id)

    context['assemble'] = assemble
    return render(request, 'assemble_graph.html', context)
@login_required
@is_admin_required
def update_assemble(request, assemble_id):
    
    context = {}
    assemble = Assemblee.objects.get(pk = assemble_id)
    form = AssembleeForm(request.POST or None, instance = assemble)
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            serv_id = form.cleaned_data['Encadreur']
            if(serv_id):
                encadreur = Personne.objects.get(user = serv_id)
                encadreur.is_encadreur = True
                encadreur.save()
            return redirect('gestion_des_assemblee')
    context['form'] = form
    return render(request, 'assemblee_add.html', context)

def add_programme(request, assemble_id):
    context = {}

    form = ProgrammeForm(request.POST or None)
    if(request.method == 'POST'):
        if(form.is_valid()):
            
            assembly = Assemblee.objects.get(pk = assemble_id)
            
            program = form.save(commit = False)
            program.assemble = assembly
            program.save()
            return redirect('assemblees_management')
    
    context['form'] = form
    return render(request,'programme_form.html', context)


def all_contacts(request):
    context = {}
    all_contact = Personne.objects.all()

    context['all_contact'] = all_contact
    return render(request, 'all_contacts.html', context)



