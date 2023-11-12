from django.contrib import admin
from .models import Unidad
from applications.edificio.models import Edificio
# Register your models here.

class Modelo_admin_unidad(admin.ModelAdmin):
    list_display = ('numero_unidad', 'edificio')
    
    list_filter = ('numero_unidad', 'edificio')
    
    search_fields = ['numero_unidad', 'edificio__nombre']

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(Unidad, Modelo_admin_unidad)