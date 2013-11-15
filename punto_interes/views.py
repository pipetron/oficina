# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from punto_interes.models import PuntoInteres, Olvera

def olvera(request):
    
    parametros = {}
    parametros['puntos_interes'] = PuntoInteres.objects.all().order_by('titulo')
    parametros['obj'] = Olvera.objects.all()[0]
    
    return render_to_response('puntos_interes/olvera.html', parametros, context_instance=RequestContext(request))

def punto_interes(request,punto_interes_id):
    
    obj = PuntoInteres.objects.get(id=punto_interes_id)
    parametros = {'obj':obj}
    
    return render_to_response('puntos_interes/contenido.html', parametros, context_instance=RequestContext(request))
