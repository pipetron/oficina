#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

class TipoPuntoInteres(models.Model):
    """
    """
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo
    
class PuntoInteres(models.Model):
    """
    """
    tipo = models.ForeignKey(TipoPuntoInteres)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.TextField()
    contenido = HTMLField()
    imagen = models.ImageField(upload_to='files/monumentos', blank=True, null=True)
    
    def __unicode__(self):
        return self.titulo

class Olvera(models.Model):
    """
    """
    titulo = models.CharField(max_length=200)
    contenido = HTMLField()
    imagen = models.ImageField(upload_to='files/olvera', blank=True, null=True)
    
    def __unicode__(self):
        return self.titulo