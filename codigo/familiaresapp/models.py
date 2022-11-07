from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre = models.CharField(max_length=30)

    parentesco = models.CharField(max_length=30)

    fecha_nacimiento = models.IntegerField()

    edad = models.IntegerField()
