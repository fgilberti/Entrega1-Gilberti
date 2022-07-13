from django.shortcuts import render
from django.http import HttpResponse

def saludo(Request):
    return HttpResponse("Bienvenido a V-Rental")

def crear_estatico(request):
    
    objeto = Cliente( marca = "Mazda" , color = "Blanco" , cantidad_pasajeros = 5 , fecha_salida = "2021-11-13" )
    objeto.save()
    
    return HttpResponse("Datos cargados con exito")


    