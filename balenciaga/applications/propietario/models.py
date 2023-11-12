from django.db import models
# Create your models here.
from django.db import models
from applications.unidades.models import Unidad  # Importa el modelo Unidad desde la aplicación unidades

class Propietario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contacto = models.CharField(max_length=100)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"