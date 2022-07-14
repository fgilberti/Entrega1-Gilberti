from django.shortcuts import render
from AppVrental.forms import RegistroFormulario, VehiculoFormulario, AlquilerFormulario, BusquedaFormulario
from AppVrental.models import Cliente


def alquiler_formulario(Request):
    if Request.method == "POST":
        pass
    else:
        registro_cliente = RegistroFormulario()
        eleccion_vehiculo = VehiculoFormulario()
        eleccion_fecha = AlquilerFormulario()
        return render(Request, "AppVrental/formulario_alquiler.html", {"registro_cliente": registro_cliente, "eleccion_vehiculo": eleccion_vehiculo, "eleccion_fecha": eleccion_fecha})
    
def busqueda_nombre(Request):
    nombre_cliente = BusquedaFormulario()
    if Request.GET:
        clientes = Cliente.objects.filter(nombre = nombre_cliente ["criterio"]).all()
        return render(Request, "AppVrental/formulario_busqueda.html", {"clientes": clientes})

    return render(Request, "AppVrental/formulario_busqueda.html", {"nombre_cliente":nombre_cliente})

