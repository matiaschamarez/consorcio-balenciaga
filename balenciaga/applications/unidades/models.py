from django.db import models
# Create your models here.

from applications.edificio.models import Edificio  # Importa el modelo Edificio desde la aplicación edificio

class Unidad(models.Model):
    
    UNIDAD_CHOICES = (
        ('A', 'Tipo A (grande)'),
        ('B', 'Tipo B (chico)'),
    )
    
    
    numero_unidad = models.CharField(max_length=10)
    tamano = models.CharField('Elija el tipo de unidad',choices=UNIDAD_CHOICES,max_length=50)
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)

    def __str__(self):
        return f"Unidad {self.numero_unidad} en {self.edificio}"
    
    class Meta:
        verbose_name_plural='Unidades'
        verbose_name= 'Unidad'