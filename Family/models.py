from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacimiento = models.DateField()
    relacion = models.CharField(max_length=40)
