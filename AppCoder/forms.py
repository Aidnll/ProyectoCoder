from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    entregado = forms.BooleanField()

class BlogFormulario(forms.Form):
    titulo=forms.CharField(max_length=100)
    codigo = forms.IntegerField()
    autor=forms.CharField(max_length=40)
    fecha=forms.DateField()
    imagen=forms.ImageField()
    contenido=forms.CharField(max_length=2500)

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat your password", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]