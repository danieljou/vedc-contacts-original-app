from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

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
        
