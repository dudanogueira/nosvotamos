from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField

import datetime

class Materia(models.Model):

    def __unicode__(self):
        return "%s - %s" % (self.tipo, self.numero_referencia)

    id_referencia = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=False, null=False)
    numero = models.IntegerField(blank=True, null=True)
    numero_referencia = models.CharField(blank=True, max_length=100)
    polemica = models.BooleanField(default=False)
    tramita = models.BooleanField(default=False)
    regime = models.CharField(blank=True, max_length=100)
    tipo = models.CharField(blank=True, max_length=100)
    autor = models.CharField(blank=True, max_length=100)
    data = models.DateField(default=datetime.datetime.today)
    ementa = models.TextField(blank=True)
    url = models.URLField(blank=True)
    url_materia_integra = models.URLField(blank=True)
    area_impacto = models.MultiPolygonField(blank=True, null=True)
    dados = JSONField(blank=True, null=True)
    # meta dados
    criado = models.DateTimeField(blank=True, auto_now_add=True, verbose_name="Criado")
    atualizado = models.DateTimeField(blank=True, auto_now=True, verbose_name="Atualizado")

class VersaoMateria(models.Model):
    material = models.ForeignKey('Materia', related_name='versoes', on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='uploads/')