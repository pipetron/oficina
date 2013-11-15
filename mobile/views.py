# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from punto_interes.models import PuntoInteres
from photologue.models import Gallery
from mobile.forms import RutaForm
from general.forms import ContactoForm
from general.models import Banner
from documentos.models import Documento
from oficina.settings import *

def inicio(request):
    parametros = {'inicio':True}
    banner = Banner.objects.filter(activo=True)[0]
    parametros['banner'] = banner
    
    documentos = Documento.objects.filter(visible=True)
    
    parametros['documentos'] = documentos
    
    return render_to_response('mobile/inicio.html', parametros,context_instance=RequestContext(request))

def galeria(request):
    parametros = {'galeria':True}
    parametros['galerias'] = Gallery.objects.filter(is_public=True)
    
    return render_to_response('mobile/galeria.html', parametros,context_instance=RequestContext(request))

def galeria_detail(request, galeria_id):
    parametros = {'galeria':True}
    parametros['galeria'] = Gallery.objects.get(id=galeria_id)
    
    return render_to_response('mobile/galeria_detail.html', parametros,context_instance=RequestContext(request))


def rutas(request):
    parametros = {'rutas':True}
    parametros['puntos'] = PuntoInteres.objects.all()
    parametros['form'] = RutaForm()
    return render_to_response('mobile/rutas2.html', parametros, context_instance=RequestContext(request))

def contacto(request):
    parametros = {'contacto':True}
    form = ContactoForm()
    if request.POST:
        form = ContactoForm(request.POST)
        if form.is_valid():
            parametros['contacto_ok'] = True
            form.save()
            form = ContactoForm()
        else:
            parametros['contacto_ko'] = True
            
    parametros['form'] = form
    return render_to_response('mobile/contacto.html', parametros,context_instance=RequestContext(request))
    