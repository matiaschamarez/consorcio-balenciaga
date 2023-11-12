from django.contrib import admin
from .models import Propietario
# Register your models here.

class Modelo_admin_propietario(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','contacto','unidad')
    
    list_filter = ('nombre','apellido','unidad')
    
    search_fields = ('nombre','apellido','unidad__nombre_unidad')

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(Propietario, Modelo_admin_propietario)

