from django.db import models
from django.contrib.auth.models import User
from main.models import *


class Numero(models.Model):
    numero = models.PositiveIntegerField()
    code_du_pays = models.PositiveIntegerField()
    disponible_sur_whatsapp = models.BooleanField()
    disponible_sur_appel = models.BooleanField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '+' + str(self.code_du_pays) + ' ' + str(self.numero)
    

class Personne(models.Model):
    assemblee = models.ForeignKey('main.Assemblee',  on_delete=models.SET_NULL, null = True, blank = True, help_text = "Si votre assemblée n'est pas disponible contactez votre encadreur")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_encadreur = models.BooleanField(default=False, null = True)
    is_encadreur = models.BooleanField(default=False, null = True)

    def __str__(self):
        non = str(self.user.last_name)
        prenom = str(self.user.first_name)
        return non.upper() + ' ' + prenom.capitalize()
    
