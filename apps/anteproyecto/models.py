from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    nombre = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.estadoN)

class AnteProyecto(models.Model):
    nombre = models.CharField(max_length=100)
    fila = models.IntegerField(blank=True, null=True)
    totalA = models.FloatField(max_length=30, blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.ManyToManyField(Estado)
    def __str__(self):
        return '{}'.format(self.nombre)

class Fila(models.Model):
    enero = models.FloatField(max_length=30, default=0, blank=True)
    febrero = models.FloatField(max_length=30, default=0, blank=True)
    marzo = models.FloatField(max_length=30, default=0, blank=True)
    abril = models.FloatField(max_length=30, default=0, blank=True)
    mayo = models.FloatField(max_length=30, default=0, blank=True)
    junio = models.FloatField(max_length=30, default=0, blank=True)
    julio = models.FloatField(max_length=30, default=0, blank=True)
    agosto = models.FloatField(max_length=30, default=0, blank=True)
    septiembre = models.FloatField(max_length=30, default=0, blank=True)
    octubre = models.FloatField(max_length=30, default=0, blank=True)
    noviembre = models.FloatField(max_length=30, default=0, blank=True)
    diciembre = models.FloatField(max_length=30, default=0, blank=True)
    diciembre = models.FloatField(max_length=30, default=0, blank=True)
    totalF = models.FloatField(max_length=30, blank=True, null=True)
    capitulo = models.ForeignKey('Capitulo', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    concepto = models.ForeignKey('Concepto', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    partidagenerica = models.ForeignKey('PartidaGenerica', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    partidaespecifica = models.ForeignKey('PartidaEspecifica', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    anteProyecto = models.ForeignKey(AnteProyecto, null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return '{}{}{}{}{}'.format(self.anteProyecto,self.capitulo,self.concepto,self.partidagenerica,self.partidaespecifica)

class Capitulo(models.Model):
    numero = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.numero)

class Concepto(models.Model):
    numero = models.IntegerField()
    capitulo = models.ForeignKey(Capitulo, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    def __str__(self):
        return '{} {}'.format(self.capitulo, self.numero)

class PartidaGenerica(models.Model):
    numero = models.IntegerField()
    concepto = models.ForeignKey(Concepto, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.concepto, self.numero)

class PartidaEspecifica(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    partidaGenerica = models.ForeignKey(PartidaGenerica, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {} {}'.format(self.partidaGenerica, self.numero, self.nombre)
