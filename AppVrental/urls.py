from django.contrib import admin
from django.urls import path
from AppVrental.views import (alquiler_formulario, formulario_busqueda)

urlpatterns = [
    path('alquiler/', alquiler_formulario),
    path('buscar/', formulario_busqueda)
]