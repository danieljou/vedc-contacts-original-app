from django.urls import path
from . import views


urlpatterns = [
    path("acceuil", views.home, name = 'home'),
    path("", views.index, name = 'index'),
    path("assemblees/", views.assemblees, name="assemblees"),
    path("assemblee_details/<assemblee_id>", views.assemblee_details, name="assemblee_details"),
    path("assemblees_management/", views.assemblees_management, name="assemblees_management")
]
