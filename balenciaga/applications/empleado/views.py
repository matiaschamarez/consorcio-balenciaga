from django.shortcuts import render
# Create your views here.
# from django.views.generic import TemplateView
# from applications.empleado.models import Empleado
# from applications.gasto_administracion.models import GastoAdministracion
# from django.db import models

# class TotalSueldosView(TemplateView):
#     template_name = 'sueldos.html'
    

#     def pagina_inicio(request):
#         return render(request, 'expensas.html')


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         # Verificar si hay empleados antes de calcular el total de sueldos
#         empleados = Empleado.objects.all()
#         if empleados:
#             total_sueldos = empleados.aggregate(total_sueldos=models.Sum('sueldo_base'))
#             context['total_sueldos'] = total_sueldos['total_sueldos']
#         else:
#             context['total_sueldos'] = 0  # O cualquier valor por defecto que desees

#         # Verificar si hay gastos administrativos antes de calcular el total
#         gastos_admin = GastoAdministracion.objects.all()
#         if gastos_admin:
#             total_gastos = gastos_admin.aggregate(total_gastos=models.Sum('monto'))
#             context['total_gastos'] = total_gastos['total_gastos']
#         else:
#             context['total_gastos'] = 0  # O cualquier valor por defecto que desees
        
#         return context
