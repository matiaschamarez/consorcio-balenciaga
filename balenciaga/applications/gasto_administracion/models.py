from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class GastoAdministracion(models.Model):
    fecha = models.DateField('Fecha')
    descripcion = RichTextField(help_text='Descripcion del gasto de administración')
    monto = models.FloatField('Monto')

    def __str__(self):
        return f'{self.monto}'
    
    class Meta:
        verbose_name_plural = 'Gastos de Administracion'
        
        
