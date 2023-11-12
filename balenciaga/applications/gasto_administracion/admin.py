from django.contrib import admin
from .models import GastoAdministracion
# Register your models here.

class Modelo_admin_gasto(admin.ModelAdmin):
    list_display = ('fecha','monto')
    
    

# Registra tu modelo y la clase personalizada en el administrador
admin.site.register(GastoAdministracion, Modelo_admin_gasto)



