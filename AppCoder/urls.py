from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inicio/', inicio, name="Inicio"),
    path('cursos/', curso, name="Curso"),
    path('carreras/', Carreras, name="Carreras"),
    path('plataforma/', Plataforma, name="Plataforma"),
    path('cursoFormulario/', cursoFormulario, name="FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("plat1/", Plat1, name="Camada"),
    path("estudianteFormulario/", estudianteFormulario, name='Estudiantes'),
    path("profesoresFormulario/", profesoresFormulario, name='Profesores'),
    path("entregablesFormulario/", entregasFormulario, name="Entregas"),
    path("blogInicio/", inicioSesion, name="Login"),
    path("registro/", registro, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("blog/", BlogMain, name="Blog"),
    path("post1/", Post1, name="Post1"),
    path("post2/", Post2, name="Post2"),
    path("post3/", Post3, name="Post3"),
    path("post4/", Post4, name="Post4"),
    path("post5/", Post5, name="Post5"),
    path("AboutMe/", AboutMe, name="AboutMe"),
    path("editarUsuario/", editarUsuario, name="EditarUsuario"),
    
    #CRUD de blogs

    path("blogs/", ListaBlog.as_view(), name='LeerBlogs'),
    #path("blog/<int:pk>", DetalleBlog.as_view(), name='BlogsDetalle'),
    path("blog/crear/", CrearBlog.as_view(), name='CrearBlogs'),
    path("blog/borrar/<int:pk>/", BorrarBlog.as_view(), name="EliminarBlogs"),
    path("blog/editar/<int:pk>/", ActualizarBlog.as_view(), name="EditarBlogs")
    
    ]