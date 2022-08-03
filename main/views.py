from django.shortcuts import render
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

    # user2 = Personne.objects.get(user = request.user)
    allnum = Numero.objects.filter(utilisateur_id = user_id)
    context['allnum'] = allnum
    # context['user2'] = user2
    return render(request, 'registration/profile.html',context)

def index(request):
    context = {}
    assemblee_count = Assemblee.objects.count()
    context['assemblee_count'] = assemblee_count

    return render(request, 'index.html',context)


def assemblees(request):
    context = {}
    assemblee_count = Assemblee.objects.count()
    assemblee = Assemblee.objects.all()

    context['assemblee_count'] = assemblee_count
    context['assemblee'] = assemblee
    return render(request, 'assemblees.html',context)

def assemblee_details(request, assemblee_id):

    context = {}
    assemblee = Assemblee.objects.get(pk = assemblee_id)
   
    serviteur = User.objects.get(pk = assemblee.Encadreur.id)
    fidele = Personne.objects.filter(assemblee_id = assemblee_id )
    
    context['serviteur'] = serviteur
    context['assemblee'] = assemblee
    context['fidele'] = fidele
    return render(request,'assamble_details.html' , context)


@login_required
@is_encadreur_required
def assemblees_management(request):
    context = {}
    return render(request, 'gerer_assemblée.html', context)
