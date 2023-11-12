from django.db import models
from applications.trabajo.models import Trabajo
# Create your models here.
class Empleado (models.Model):

    horario_choices = (
        ('Mañana', 'Mañana'),
        ('Tarde','Tarde'),
        ('Noche','Noche'),
    )
    
    
    nombre = models.CharField('Nombre', max_length=50,null=False)
    apellido = models.CharField('Apellido', max_length=50,null=False)
    cuil = models.CharField('Cuil', max_length=13,unique=True,null=False)
    telefono = models.CharField('Telefono', max_length=50,unique=True)
    domicilio = models.CharField('Domicilio', max_length=50,help_text='Ej: Calle y número')
    fecha_nac = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False)
    email = models.EmailField('Email', max_length=254,null=False,unique=True)
    sueldo_base = models.FloatField('Sueldo base',null=False)
    horario = models.CharField('Horario', max_length=50,null=False,choices=horario_choices)
    trabajo = models.ForeignKey(Trabajo,on_delete=models.CASCADE,default='1')
    
    def __str__(self):
        return self.nombre + " - " + self.apellido