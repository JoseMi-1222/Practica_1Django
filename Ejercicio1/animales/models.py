from django.db import models
from django.conf import settings

# Modelo 1: Protectora
class Protectora(models.Model):
    nombre = models.CharField(max_length=200)       
    descripcion = models.TextField()                
    fecha_creacion = models.DateTimeField() 

    def __str__(self):
        return self.nombre

# Modelo 2: Colaborador
class Colaborador(models.Model):
    nombre = models.CharField(max_length=200)       
    cargo = models.CharField(max_length=100)        
    fecha_entrada_protectora = models.DateTimeField() 

    def __str__(self):
        return self.nombre

# Modelo 3: Animal
class Animal(models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)       
    tipo = models.CharField(max_length=100)         

    def __str__(self):
        return self.nombre