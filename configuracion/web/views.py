from django.shortcuts import render

from web.formularios.formularioMedico import formularioMedico

# Create your views here.
#render (renderizar) es PINTAR 
def Home(request):
    return render(request,'index.html')

def Medicos(request):

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
            print(datos)

    return render(request,'registromedicos.html',diccionario)
