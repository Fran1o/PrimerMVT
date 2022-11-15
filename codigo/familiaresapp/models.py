from django.db import models

# Create your models here.
class Familia(models.Model):

    nombre = models.CharField(max_length=30)

    fecha_nacimiento = models.DateField()

    edad = models.IntegerField()

class Primos(models.Model):

    nombre = models.CharField(max_length=30)

    fecha_nacimiento = models.DateField()

    edad = models.IntegerField()

class Tios(models.Model):
    
    nombre = models.CharField(max_length=30)

    fecha_nacimiento = models.DateField()

    edad = models.IntegerField()
