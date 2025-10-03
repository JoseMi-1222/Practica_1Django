from django.urls import path
from .views import inicio, lista_clientes, lista_membresias, lista_clases

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('membresias/', lista_membresias, name='lista_membresias'),
    path('clases/', lista_clases, name='lista_clases'),
]   