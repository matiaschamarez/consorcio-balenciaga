from django.db import models

# Create your models here.
class Edificio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.direccion}'