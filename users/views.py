from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .decorators import *

# Create your views here.




def add_form(request):
    context = {}
    role_form = PersonneForm(request.POST or None)
    form_user = FormUser(request.POST or None)

    if(request.method == 'POST'):
        if(role_form.is_valid() and form_user.is_valid()):
            account = form_user.save()
            role = role_form.save(commit  = False)
            role.user = account
            role.save()
            messages.success(request, "Enregistrement éffectué avec succès")
            return redirect('home')
        else:
             messages.warning(request, "Veuillez compléter le formulaire")

    context['form_user'] = form_user 
    context['role_form'] = role_form 
    context['users'] = True
    return render(request,'form.html',context)

@login_required
def user_mod(request):
    account = Personne.objects.get(pk = request.user.id)
    user = User.objects.get(pk = account.user.id)

    context = {}
    role_form = PersonneForm(request.POST or None, instance = account)
    form_user = FormUser(request.POST or None, instance = user)

    if(request.method == 'POST'):
        if(role_form.is_valid() and form_user.is_valid()):
            account = form_user.save()
            role = role_form.save(commit  = False)
            role.user = account
            role.save()
            messages.success(request, "Modification éffectuée avec succès")
            return redirect('home')
        else:
             messages.warning(request, "Veuillez compléter le formulaire")

    context['form_user'] = form_user 
    context['role_form'] = role_form 
    context['mod'] = True
    
    return render(request,'form.html',context)





@login_required
def add_numero(request):
    context = {}
    form = FromNumero()
    if(request.method == 'POST'):
        form = FromNumero(request.POST)
        if(form.is_valid()):
            numero = form.save(commit = False)
            numero.utilisateur = request.user
            numero.save()
            return redirect('home')

    context['form'] = form
    return render(request, 'form_numero.html', context)

@login_required
def delete_num(request, num_id):
    num = Numero.objects.get(pk = num_id)
    num.delete()
    return redirect('home')


@login_required
def update_num(request, num_id):
    context = {}
    num = Numero.objects.get(pk = num_id)
   
    form = FromNumero(instance = num)
    if(request.method == 'POST'):
        form = FromNumero(request.POST, instance = num)
        if(form.is_valid()):
            numero = form.save(commit = False)
            numero.utilisateur = request.user
            numero.save()
            return redirect('home')
    context['mod'] = True
    context['form'] = form
    return render(request, 'form_numero.html', context)


def user_details(request, user_id):
    context = {}
    user_account = User.objects.get(pk = user_id)
    account = Personne.objects.get(user = user_account)
    allnum = Numero.objects.filter(utilisateur_id = user_id)
    back = request.GET['back']

    context['account'] = account
    context['user_account'] = user_account
    context['allnum'] = allnum
    context['back'] = back
    return render(request, 'personne_details.html', context)