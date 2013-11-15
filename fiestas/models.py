#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

class AmbitoFiesta(models.Model):
    """
    Ámbito de una fiesta
    """
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo
    
    def fiestas(self):
        return Fiesta.objects.filter(ambito=self).order_by('fecha_inicio')
        
class Fiesta(models.Model):
    """
    Clase que representa una fiesta
    """
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    contenido = HTMLField()
    imagen = models.ImageField(upload_to='files/fiestas', blank=True, null=True)
    ambito = models.ForeignKey(AmbitoFiesta)
    
    def __unicode__(self):
        return self.titulo
    
    def programacion(self):
        return Programa.objects.filter(fiesta=self)

class Programa(models.Model):
    """
    Clase que representa un programa de una fiesta
    """
    fiesta = models.ForeignKey(Fiesta)
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    
    def __unicode__(self):
        return u"%s: %s" % (self.fiesta,self.titulo)
    
