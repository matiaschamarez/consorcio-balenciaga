from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Arreglo(models.Model):
    fecha = models.DateField()
    descripcion = RichTextField(help_text='Ingrese la descripción del arreglo')
    costo = models.FloatField('Costo')


    def __str__(self):
        return f'{self.fecha} - {self.costo}'