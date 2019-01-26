from django.db import models

# Create your models here.

class Administrador(models.Model):
	nombre = models.CharField(max_length=50) 
	apellidoP = models.CharField(max_length=20)
	apellidoM = models.CharField(max_length=20)

	correo = models.EmailField()

	sexo = models.CharField(max_length=10)
	edad = models.IntegerField()
	nacimiento = models.DateField() 
	telefono = models.IntegerField()
	domicilio = models.TextField()
