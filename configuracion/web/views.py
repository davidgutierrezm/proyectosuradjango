from django.shortcuts import render

from web.formularios.formularioMedico import formularioMedico
from web.formularios.formularioPacientes import formularioPacientes

from web.models import Medicos
from web.models import Pacientes



# Create your views here.
#render (renderizar) es PINTAR 
def Home(request):
    return render(request,'index.html')

def MedicosVista(request):

    #debo utilizar la clase formularioMedico
    # Creamos asi un objeto 
    formulario = formularioMedico()
    diccionario = {
        "formulario" : formulario
    }

    #Activar la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=formularioMedico(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            #llevar mis datos hacia la BD
            medicoNuevo = Medicos (
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tarjeta=datos["tarjetaProfesional"],
                especialidad=datos["especialidad"],
                jornada=datos["jornada"],
                contacto=datos["contacto"],
                sede=datos["sede"]
            )
            medicoNuevo.save()
            print("Sus datos han sido guardados con éxito")

    return render(request,'registromedicos.html',diccionario)

def PacientesVista(request):

    #debo utilizar la clase formularioMedico
    # Creamos asi un objeto 
    formulario = formularioPacientes()
    diccionario = {
        "formulario" : formulario
    }

    #Activar la recepcion de datos
    if request.method=='POST':
        #validar si los datos son correctos
        datosRecibidos=formularioPacientes(request.POST)
        if datosRecibidos.is_valid():
            #capturar los datos
            datos=datosRecibidos.cleaned_data
            pacienteNuevo = Pacientes (
                nombres=datos["nombre"],
                apellidos=datos["apellidos"],
                cedula=datos["cedula"],
                tipo=datos["tipo_afiliado"],
                regimen=datos["regimen"],
                grupo=datos["grupo_ingreso"],
                celular=datos["celular"],
                correo=datos["correo"]
            )
            pacienteNuevo.save()
            print("Sus datos han sido guardados con éxito")

    return render(request,'registropacientes.html',diccionario)
