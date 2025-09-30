from django.db import models
from django.conf import settings
# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    numero_camiseta = models.IntegerField()

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, related_name='partidos_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipo, related_name='partidos_visitante', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estadio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} on {self.fecha}"