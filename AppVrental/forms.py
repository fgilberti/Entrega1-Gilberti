from django import forms

class RegistroFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    dni = forms.CharField()

class VehiculoFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    cantidad_de_asientos = forms.IntegerField()
    precio_por_dia = forms.IntegerField()

class AlquilerFormulario(forms.Form):
    fecha_de_retiro = forms.DateField()
    fecha_de_devolucion = forms.DateField()

class BusquedaFormulario(forms.Form):
    criterio = forms.CharField()

    