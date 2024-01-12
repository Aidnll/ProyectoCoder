from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *



def inicio (request):
    return render (request, "AppCoder/inicio.html")

def curso (request):
    return render (request, "AppCoder/cursos.html")

def Carreras(request):
    return render (request, "AppCoder/carreras.html")

def Plataforma(request):
    return render (request,"AppCoder/plataforma.html")

def Plat1(request):
    return render(request, "AppCoder/plat1.html")

def cursoFormulario(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info['curso'], camada=info['camada'])

            curso.save()

            return render(request, "AppCoder/inicio.html")
        
    else:
    
        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"form1":formulario1})


def busquedaCamada(request):

    return render(request, "AppCoder/plat1.html")

def resultados(request):

    if request.GET["camada"]:

        camada=request.GET["camada"]
        cursos=Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoder/plat1.html", {"cursos":cursos, "camada":camada})
    
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


def estudianteFormulario(request):

    if request.method == "POST":

        formulario2 = EstudianteFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            estudiante = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])

            estudiante.save()

            return render(request, "AppCoder/plataforma.html")
        
    else:
    
        formulario2 = EstudianteFormulario()

    return render(request, "AppCoder/estudianteFormulario.html", {"form2":formulario2})



def profesoresFormulario(request):

    if request.method == "POST":

        formulario3 = ProfesoresFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            profesor = Profesor(nombre=info['nombre'], apellido=info['apellido'], email=info['email'], profesion=info['profesion'])

            profesor.save()

            return render(request, "AppCoder/plataforma.html")
        
    else:
    
        formulario3 = ProfesoresFormulario()

    return render(request, "AppCoder/profesoresFormulario.html", {"form3":formulario3})


def entregasFormulario(request):

    if request.method == "POST":

        formulario4 = EntregablesFormulario(request.POST)

        if formulario4.is_valid():

            info = formulario4.cleaned_data

            entrega = Entregable(nombre=info['nombre'], fecha=info['fecha'], entregado=info['entregado'])

            entrega.save()

            return render(request, "AppCoder/plataforma.html")
        
    else:
    
        formulario4 = EntregablesFormulario()

    return render(request, "AppCoder/entregablesFormulario.html", {"form4":formulario4})