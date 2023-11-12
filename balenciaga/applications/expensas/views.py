from django.shortcuts import render
from decimal import Decimal
from django.db.models import Sum
from .models import Expensa

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from applications.empleado.models import Empleado
from applications.gasto_administracion.models import GastoAdministracion
from django.db import models
from applications.unidades.models import Unidad 

class TotalSueldosView(TemplateView):
    template_name = 'finance.html'
    

    def pagina_inicio(request):
        return render(request, 'expensas.html')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Calcular el total de sueldos
        total_sueldos = Empleado.objects.aggregate(total_sueldos=Sum('sueldo_base'))['total_sueldos'] or 0

        # Calcular el total de gastos de administración
        total_gastos = GastoAdministracion.objects.aggregate(total_gastos=Sum('monto'))['total_gastos'] or 0

        # Obtener la cantidad de unidades
        cantidad_unidades = Unidad.objects.count() or 1  # Asegura que no sea cero

        gasto_unidad =(total_sueldos+total_gastos)/cantidad_unidades
        # Calcular el promedio de sueldos y gastos por unidad
        promedio_sueldos = total_sueldos / cantidad_unidades
        promedio_gastos = total_gastos / cantidad_unidades

        context['total_sueldos'] = total_sueldos
        context['total_gastos'] = total_gastos
        context['gasto_unidad'] = gasto_unidad
        context['promedio_gastos'] = promedio_gastos

        return context


