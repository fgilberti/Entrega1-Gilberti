from django.db import models
from django.forms import DateField

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8)

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    cant_asientos = models.IntegerField()
    precio_dia = models.IntegerField()

class Alquiler(models.Model):
    fecha_retiro = DateField()
    fecha_entrega = DateField()
    