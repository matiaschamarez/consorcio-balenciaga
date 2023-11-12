from django.contrib import admin
from .models import Arreglo
# Register your models here.

class Modelo_admin_arreglo(admin.ModelAdmin):
    list_display = ('fecha','costo',)
    

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(Arreglo, Modelo_admin_arreglo)