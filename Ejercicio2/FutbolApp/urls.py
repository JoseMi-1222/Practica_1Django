from django.shortcuts import render
from .models import Equipo, Jugador, Partido
from django.urls import path
from . import views

# Vista para la página de inicio
def inicio(request):
    return render(request, 'futbol/inicio.html')    

# Vista para listar todos los equipos
def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/lista_equipos.html', {'lista_de_equipos': equipos})  

# Vista para listar todos los jugadores
def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/lista_jugadores.html', {'lista_de_jugadores': jugadores})

# Vista para listar todos los partidos
def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'futbol/lista_partidos.html', {'lista_de_partidos': partidos})

urlpatterns = [
    path('', inicio, name='inicio'),
    path('equipos/', lista_equipos, name='lista_equipos'),
    path('jugadores/', lista_jugadores, name='lista_jugadores'),
    path('partidos/', lista_partidos, name='lista_partidos'),
]
