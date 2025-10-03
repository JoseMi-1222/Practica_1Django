from django.shortcuts import render
from .models import Cliente, Membresia, Clase

# Create your views here.

def inicio(request):
    return render(request, 'gym/inicio.html')    

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gym/lista_clientes.html', {'lista_de_clientes': clientes})

def lista_membresias(request):  
    membresias = Membresia.objects.all()
    return render(request, 'gym/lista_membresias.html', {'lista_de_membresias': membresias})   
 
def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'gym/lista_clases.html', {'lista_de_clases': clases})