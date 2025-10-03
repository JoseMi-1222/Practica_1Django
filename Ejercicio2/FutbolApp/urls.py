from django.urls import path
from .views import inicio, lista_equipos, lista_jugadores, lista_partidos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('equipos/', lista_equipos, name='lista_equipos'),
    path('jugadores/', lista_jugadores, name='lista_jugadores'),
    path('partidos/', lista_partidos, name='lista_partidos'),
]
