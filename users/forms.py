import django.db
from .models import *
from django import forms
from django.forms import (
    CheckboxInput,TextInput,ModelForm,EmailInput, 
    NumberInput, DateInput, 
    BooleanField, Select, FileInput,
    Textarea,
    
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings



class FormUser(UserCreationForm):
    email = forms.EmailField(required=True, max_length=100)
    last_name = forms.CharField(required=True, max_length=100, label="Nom")
   
    
    class Meta:
        model = User
        fields = ('username','last_name','first_name','email','password1','password2')
        widgets = {
            'last_name': forms.TextInput()
        }

class PersonneForm(forms.ModelForm):
    
    class Meta:
        model = Personne
        exclude = ('user','is_encadreur',)

        widgets = {
            'assemblee' : forms.Select(attrs={
                'class' : 'form-select'
            })
        }


class FromNumero(forms.ModelForm):
    class Meta:
        model = Numero
        exclude = ('utilisateur',)