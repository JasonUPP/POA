from django.db import models

class AnteProyecto(models.Model):
    capitulo = models.CharField(max_length=30, null=True)
    partida = models.CharField(max_length=30, null=True)
    enero = models.FloatField(max_length=30)
    febrero = models.FloatField(max_length=30)
    marzo = models.FloatField(max_length=30)
    abril = models.FloatField(max_length=30)
    mayo = models.FloatField(max_length=30)
    junio = models.FloatField(max_length=30)
    julio = models.FloatField(max_length=30)
    agosto = models.FloatField(max_length=30)
    septiembre = models.FloatField(max_length=30)
    octubre = models.FloatField(max_length=30)
    noviembre = models.FloatField(max_length=30)
    diciembre = models.FloatField(max_length=30)
    diciembre = models.FloatField(max_length=30)
    total = models.FloatField(max_length=30)
