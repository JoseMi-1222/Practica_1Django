from django.db import models
from django.conf import settings

# Create your models here.

class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre  
    
class Membresia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - {self.cliente.nombre}"
    
class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.DateTimeField()

    def __str__(self):
        return self.nombre