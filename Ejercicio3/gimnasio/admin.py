from django.contrib import admin
from .models import Cliente, Membresia, Clase

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Membresia)
admin.site.register(Clase)