from django.urls import path
from . import views

urlpatterns = [
    
    path("form/", views.add_form, name="user_form"),
    path('upadate', views.user_mod, name = 'user_update'),
    
    path("add_numero/", views.add_numero, name="add_numero"),
    path("delete_num/<num_id>", views.delete_num, name="delete_num"),
    path("update_num/<num_id>", views.update_num, name="update_num"),
    path("user_details/<user_id>", views.user_details, name="user_details")
]
