from django.shortcuts import render
from .models import Animal, Protectora, Colaborador
from django.urls import path
from . import views

# Vista para la página de inicio
def inicio(request):
    return render(request, 'animals/inicio.html')

# Vista para listar todos los animales
def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animals/lista_animales.html', {'lista_de_animales': animales})

# Vista para listar todas las protectoras
def lista_protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'animals/lista_protectoras.html', {'lista_de_protectoras': protectoras})

# Vista para listar todos los colaboradores
def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'animals/lista_colaboradores.html', {'lista_de_colaboradores': colaboradores})

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('animales/', views.lista_animales, name='lista_animales'),
    path('protectoras/', views.lista_protectoras, name='lista_protectoras'),
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
]
