from django.shortcuts import render
from .models import Equipo, Jugador, Partido

# Create your views here.

def inicio(request):
    return render(request, 'futbol/inicio.html')    

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/lista_equipos.html', {'lista_de_equipos': equipos})

def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/lista_jugadores.html', {'lista_de_jugadores': jugadores})

def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'futbol/lista_partidos.html', {'lista_de_partidos': partidos})   

