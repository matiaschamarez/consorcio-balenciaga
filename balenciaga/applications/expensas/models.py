from django.db import models
from django.shortcuts import render
from applications.arreglo.models import Arreglo
from applications.empleado.models import Empleado
from ckeditor.fields import RichTextField
# Create your models here.
from applications.unidades.models import Unidad  # Importa el modelo Unidad desde la aplicación unidades

class Expensa(models.Model):
    fecha = models.DateField()
    descripcion = RichTextField(help_text='Descripcion')
    unidades = models.ManyToManyField(Unidad)
    
    
    
    def __str__(self):
        return f"Fecha de expensa {self.fecha}"