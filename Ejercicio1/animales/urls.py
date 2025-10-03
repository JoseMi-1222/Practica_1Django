from django.urls import path
from .views import inicio, lista_animales, lista_protectoras, lista_colaboradores

urlpatterns = [
    path('', inicio, name='inicio'),
    path('animales/',lista_animales, name='lista_animales'),
    path('protectoras/', lista_protectoras, name='lista_protectoras'),
    path('colaboradores/', lista_colaboradores, name='lista_colaboradores'),
]
