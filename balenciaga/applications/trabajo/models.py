from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Trabajo (models.Model):
    nombre = models.CharField('Nombre', max_length=50,null=False)
    descripcion = RichTextField(help_text='Ingrese la descripción del trabajo')
    
    def __str__(self):
        return f'{self.nombre}'
