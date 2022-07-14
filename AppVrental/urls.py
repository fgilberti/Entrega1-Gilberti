from django.contrib import admin
from django.urls import path
from AppVrental.views import (alquiler_formulario, busqueda_nombre)

urlpatterns = [
    path('alquiler/', alquiler_formulario),
    path('buscar/', busqueda_nombre)
]