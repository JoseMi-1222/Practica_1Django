from django.shortcuts import render

# Create your views here.
from .models import Animal, Protectora, Colaborador

def inicio(request):
    return render(request, 'animals/inicio.html')

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animals/lista_animales.html', {'lista_de_animales': animales})

def lista_protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'animals/lista_protectoras.html', {'lista_de_protectoras': protectoras})

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'animals/lista_colaboradores.html', {'lista_de_colaboradores': colaboradores})