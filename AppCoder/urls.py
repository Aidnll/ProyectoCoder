from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('cursos/', curso, name="Curso"),
    path('carreras/', Carreras, name="Carreras"),
    path('plataforma/', Plataforma, name="Plataforma"),
    path('cursoFormulario/', cursoFormulario, name="FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("plat1/", Plat1, name="Camada"),
    path("estudianteFormulario/", estudianteFormulario, name='Estudiantes'),
    path("profesoresFormulario/", profesoresFormulario, name='Profesores'),
    path("entregablesFormulario/", entregasFormulario, name="Entregas")
    
    ]