#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class TipoEvento(models.Model):
    """
    Tipo de evento
    """
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo
        
class Evento(models.Model):
    """
    Clase que representa un evento
    """
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    contenido = HTMLField()
    imagen = models.ImageField(upload_to='files/eventos', blank=True, null=True)
    tipo = models.ForeignKey(TipoEvento)
    
    def __unicode__(self):
        return self.titulo
    
    def programacion(self):
        return Programa.objects.filter(evento=self)
    
class Programa(models.Model):
    """
    Clase que representa un programa de un evento
    """
    evento = models.ForeignKey(Evento)
    titulo = models.CharField(max_length=100)
    hora = models.TimeField()
    
    def __unicode__(self):
        return u"%s: %s" % (self.evento,self.titulo)