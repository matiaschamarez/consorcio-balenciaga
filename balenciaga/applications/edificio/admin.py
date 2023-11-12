from django.contrib import admin
from .models import Edificio
# Register your models here.

class Modelo_admin_edificio(admin.ModelAdmin):
    list_display = ('nombre','direccion')
    
    search_fields = ('nombre','direccion')

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(Edificio, Modelo_admin_edificio)