from functools import wraps
from django.http import HttpResponseRedirect
from .models import *



def is_admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile = request.user
        account = Personne.objects.get(user = profile.id)
        user_type = account.role
        if(user_type == 'Administrateur'):
            return function(request, *args, **kwargs)
        else:
            a = 0
            return HttpResponseRedirect('/')
    return wrap

def is_encadreur_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        profile = request.user
        account = Personne.objects.get(user = profile.id)
        user_type = account.is_encadreur
        if(user_type):
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    return wrap

