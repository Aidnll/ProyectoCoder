from django.db import models

class Curso(models.Model):

    def _srt_(self):
        return f"Nombre: {self.nombre} ---- Camada: {self.camada}"

    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiante(models.Model):

    def _srt_(self):
        return f"Nombre: {self.nombre} ---- Apellido: {self.apellido}"

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):

    def _srt_(self):
        return f"Nombre: {self.nombre} ---- Apellido: {self.apellido}"

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Entregable(models.Model):

    def _srt_(self):
        return f"Nombre: {self.nombre} ---- Fecha: {self.fecha}"

    nombre=models.CharField(max_length=40)
    fecha=models.DateField()
    entregado=models.BooleanField()

class Blog(models.Model):

    def _srt_(self):
        return f"Titulo: {self.titulo} ---- Autor: {self.Autor}"
    
    titulo=models.CharField(max_length=100)
    codigo=models.IntegerField()
    autor=models.CharField(max_length=40)
    fecha=models.DateField()
    imagen=models.ImageField()
    contenido=models.CharField(max_length=2500)
