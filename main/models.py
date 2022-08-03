from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Assemblee(models.Model):

    SRVT = 'Serviteur'
    PAST = 'Pasteur'
    DPT = 'Délégué Pastoral'
    DIACRE = 'Diacre'
    ENCADREUR_CHOICE = [
        (SRVT, 'Serviteur'),
        (PAST, 'Pasteur'),
        (DPT, 'Délégué Pastoral'),   
        (DIACRE, 'Diacre'),   
    ]

    Nom_assemblee = models.CharField(max_length=80)
    Encadreur = models.ForeignKey(User, related_name = 'Encandreur', on_delete=models.SET_NULL, blank = True, null =True)
    Type_encadreur = models.CharField(choices = ENCADREUR_CHOICE, max_length=50, default = SRVT)
    coordonnees_localisation = models.TextField(null = True, blank = True)
    pays = models.CharField( max_length=8)
    ville = models.CharField( max_length=50)
    Quartier = models.CharField(max_length=50, null = True, blank = True)

    
    

    def __str__(self):
        return self.Nom_assemblee
    

class PhotoAssemble(models.Model):
    Image = models.ImageField( upload_to='PhotoAssemblee')
    assemblee = models.ForeignKey("Assemblee", on_delete=models.CASCADE)

class Programme(models.Model):
    assemble = models.ForeignKey("Assemblee", related_name='assamble_programme', on_delete=models.CASCADE)

    JOUR_CHOICES = [
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
        ('Dimanche', 'Dimanche'),
    ]

    jour = models.CharField(choices = JOUR_CHOICES, max_length=50)
    Heure = models.TimeField(auto_now=False, auto_now_add=False)
    Titre = models.CharField(max_length=50, null = True)