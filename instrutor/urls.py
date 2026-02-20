from django.urls import path
from instrutor import views

app_name = "instrutor"

urlpatterns = [
    path("lista/", views.listar, name="listar"),
]