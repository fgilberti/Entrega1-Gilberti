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
    
    
def formulario_busqueda(Request):

    if Request.GET["criterio"]:
        clientes = Cliente.objects.filter(nombre = "criterio").all()
        return render(Request, "AppVrental/formulario_busqueda.html", {"clientes": clientes})
    else:
        respuesta = "No se envió ningun dato"
        
    return render(Request, "AppVrental/formulario_busqueda.html", {"formulario_busqueda": respuesta})

