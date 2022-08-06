from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'username': forms.TextInput(attrs={
                'Placeholder':'Votre nom d\'utilisateur',
            }),

            'password': forms.TextInput(attrs={
                'Placeholder':'Votre mot de passe',
            }),
        }
        

class AssembleeForm(forms.ModelForm):
    
    class Meta:
        model = Assemblee
        fields = ("__all__")
        
        widgets = {
            'Encadreur': forms.Select(attrs={
                'class':'form-select',
            }),

            'Type_encadreur': forms.Select(attrs={
                'class':'form-select',
            }),

            'Continent': forms.Select(attrs={
                'class':'form-select',
            }),
        }

class ProgrammeForm(forms.ModelForm):
    
    class Meta:
        model = Programme
        exclude = ('assemble',)
        widgets = {
            'jour' : forms.Select(attrs = {
                'class' : 'form-select'
            }),
            'Heure' : forms.TimeInput(attrs={'type': 'time'})

        }
