from django.contrib import admin
from .models import Empleado

class Modelo_admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido','sueldo_base','trabajo','horario')
    
    list_filter = ('nombre','apellido','trabajo','horario')
    
    search_fields = ['nombre', 'apellido', 'trabajo__nombre', 'horario']

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(Empleado, Modelo_admin)





