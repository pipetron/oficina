# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from eventos.models import Evento

def eventos(request):
    
    parametros = {}
    parametros['eventos_obj'] = Evento.objects.all()
    parametros['eventos'] = True
    
    return render_to_response('eventos/eventos.html', parametros, context_instance=RequestContext(request))

def evento_detail(request,evento_id):
    
    evento = Evento.objects.get(id=evento_id)
    parametros = {'evento':evento}
    parametros['eventos'] = True
    
    return render_to_response('eventos/evento_detail.html', parametros, context_instance=RequestContext(request))