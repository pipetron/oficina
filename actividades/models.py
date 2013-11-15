#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import ho.pisa as pisa
import cStringIO as StringIO

from django.template.loader import render_to_string
from django.db import models

from cmisutils.cmis import CMISConnector
from settings import CMIS_URL, CMIS_USER, CMIS_PWD, RESERVAS_FOLDER_ID
from tinymce.models import HTMLField

# Create your models here.
class TipoActividad(models.Model):
    """
    Tipo de actividad
    """
    titulo = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.titulo
        
class Actividad(models.Model):
    """
    Clase que representa una actividad que se realiza en la oficina
    """
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    contenido = HTMLField()
    imagen = models.ImageField(upload_to='files/actividades', blank=True, null=True)
    tipo = models.ForeignKey(TipoActividad)
    
    def __unicode__(self):
        return self.titulo

class Reserva(models.Model):
    """
    Clase que representa la reserva de una actividad
    """
    actividad = models.ForeignKey(Actividad)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    nombre = models.CharField(max_length=200)
    telefono = models.CharField("Teléfono",max_length=9)
    correo = models.EmailField()
    informacion = models.TextField("Información")
    docid = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s del %s al %s (%s)" % (self.actividad,self.fecha_inicio.strftime("%d/%m/%Y %H:%M"),self.fecha_fin.strftime("%d/%m/%Y %H:%M"),self.nombre)
        