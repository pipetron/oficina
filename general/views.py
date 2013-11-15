#!/usr/bin/python
# -*- coding: utf-8 -*-
import mimetypes

from os import path

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from general.models import Banner
from general.forms import ContactoForm
from documentos.models import Documento
from settings import *

def inicio(request):
    """
    Página de inicio
    """
    parametros = {'inicio':True}
    banner = Banner.objects.filter(activo=True)[0]
    parametros['banner'] = banner
    
    return render_to_response('general/inicio.html', parametros,context_instance=RequestContext(request))

def contacto(request):
    """
    Página de contacto y cómo llegar
    """
    parametros = {'contacto':True}
    form = ContactoForm()
    
    
    if request.POST:
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactoForm()
            parametros["form_enviado"] = True
    
    parametros['form'] = form
    
    return render_to_response('general/contacto.html', parametros,context_instance=RequestContext(request))

def documentos(request):
    """
    Página de documentos de interés
    """
    parametros = {'docs':True}
    #Conexion con gestor documental
    docs_obj = Documento.objects.filter(visible=True)
    
    documentos = []
    for doc in docs_obj:
        titulo = doc.titulo
        docid = doc.id
        
        mimetype = mimetypes.guess_type(doc.archivo.name)[0]
        extension = mimetypes.guess_extension(mimetype)
        
        documentos.append({'titulo':titulo,'id':docid, 'extension':extension[1:]})
    
    parametros['documentos'] = documentos
    
    return render_to_response('general/documentos.html', parametros,context_instance=RequestContext(request))

def descargar_documento(request,id):
    """
    Descarga documento desde el gestor documental
    """
    doc = Documento.objects.get(id=id)
    response = HttpResponse(doc.archivo)
    filename = path.basename(doc.archivo.name)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response['Content-Type'] = mimetypes.guess_type(filename)[0]
    
    return response