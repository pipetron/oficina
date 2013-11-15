# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from fiestas.models import Fiesta, AmbitoFiesta

def ver_fiestas(request):
    
    ambitos = AmbitoFiesta.objects.all()
    parametros = {'fiestas_sel':True, 'ambitos':ambitos}
    
    return render_to_response('fiestas/fiestas.html', parametros, context_instance=RequestContext(request))

def fiesta_detail(request, fiesta_id):
    
    fiesta = Fiesta.objects.get(id=fiesta_id)
    parametros = {'fiestas_sel':True, 'fiesta':fiesta}
    parametros['proximas_fiestas'] = Fiesta.objects.filter(fecha_inicio__gt=fiesta.fecha_fin)
    
    return render_to_response('fiestas/fiesta_detail.html', parametros, context_instance=RequestContext(request))