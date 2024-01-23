from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicioSesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
                return redirect("LeerBlogs")
        else:
            return redirect("Registro")
    else:
        form = AuthenticationForm()
    return render(request, "AppCoder/blogInicio.html", {"formulario":form})
    

def registro(request):
    if request.method == "POST":
        formR = UsuarioRegistro(request.POST)
        if formR.is_valid():

            username = formR.cleaned_data["username"]
            formR.save()
            return redirect("Login")
    
    else:
        formR = UsuarioRegistro()
    return render(request, "AppCoder/registro.html", {"formularioR":formR})

@login_required
def editarUsuario (request):
    usuario = request.user

    if request.method == "POST":
        formu = FormularioEditar(request.POST)

        if formu.is_valid():
            info = formu.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info['password1'])
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']

            usuario.save()
            return render(request, 'AppCoder/inicio.html')
    
    else:
        formu = FormularioEditar(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
            })
    return render (request, "AppCoder/editarPerfil.html", {"formularioU":formu, "usuario":usuario })

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

def AboutMe(request):
    return render(request, "AppCoder/AboutMe.html")

@login_required
def BlogMain(request):
    return redirect("LeerBlogs")

@login_required
def Post1(request):
    return render (request, "AppCoder/post1.html")

@login_required
def Post2(request):
    return render (request, "AppCoder/post2.html")

@login_required
def Post3(request):
    return render (request, "AppCoder/post3.html")

@login_required
def Post4(request):
    return render (request, "AppCoder/post4.html")

@login_required
def Post5(request):
    return render (request, "AppCoder/post5.html")

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


class ListaBlog(LoginRequiredMixin, ListView):
    model = Blog

class CrearBlog(LoginRequiredMixin, CreateView):
    model = Blog
    success_url ="AppCoder/blog.html"
    fields = ["titulo", "codigo","autor","fecha","imagen", "contenido"]

class ActualizarBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    success_url ="AppCoder/blog.html"
    fields = ["titulo", "codigo","autor","fecha","imagen", "contenido"]

class BorrarBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url ="AppCoder/blog.html"
