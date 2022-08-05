from django.urls import path
from . import views


urlpatterns = [
    path("acceuil", views.home, name = 'home'),
    path("", views.index, name = 'index'),
    path("assemblees/", views.assemblees, name="assemblees"),
    path("assemblee_details/<assemblee_id>/", views.assemblee_details, name="assemblee_details"),
    path("assemblees_management/", views.assemblees_management, name="assemblees_management"),
    path("gestion_des_assemblee/", views.gestion_des_assemblee, name="gestion_des_assemblee"),
    path("assemnble_add/", views.assemnble_add, name="assemnble_add"),
    path("add_programme/", views.add_programme, name="add_programme"),

    path("all_contacts/", views.all_contacts, name="all_contacts"),
    
]
