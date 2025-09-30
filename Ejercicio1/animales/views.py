from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Animal

def inicio(request):
    return render(request, 'animals/inicio.html')

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'animals/lista_animales.html', {'lista_de_animales': animales})

def lista_protectoras(request):
    from .models import Protectora
    protectoras = Protectora.objects.all()
    return render(request, 'animals/lista_protectoras.html', {'lista_de_protectoras': protectoras})

def lista_colaboradores(request):
    from .models import Colaborador
    colaboradores = Colaborador.objects.all()
    return render(request, 'animals/lista_colaboradores.html', {'lista_de_colaboradores': colaboradores})