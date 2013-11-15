# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from actividades.models import Actividad
from actividades.forms import ReservaForm

def actividades(request):
    
    parametros = {}
    parametros['actividades_obj'] = Actividad.objects.all()
    parametros['actividades'] = True
    
    return render_to_response('actividades/actividades.html', parametros, context_instance=RequestContext(request))

def actividad_detail(request, actividad_id):
    
    parametros = {}
    parametros['actividad'] = Actividad.objects.get(id=actividad_id)
    parametros['form'] = ReservaForm()
    parametros['actividades'] = True
    
    return render_to_response('actividades/actividad_detail.html', parametros, context_instance=RequestContext(request))

def reservar(request):
    
    datos = request.POST.copy()
    actividad = Actividad.objects.get(id=datos.get('actividad'))
    parametros = {'actividad':actividad}
    form = ReservaForm(datos)
    
    if form.is_valid():
        reserva = form.save()
        parametros['reserva'] = reserva
        return render_to_response('actividades/reserva_ok.html', parametros, context_instance=RequestContext(request))
    else:
        parametros['form'] = form
        return render_to_response('actividades/form_reserva.html', parametros, context_instance=RequestContext(request))
    return HttpResponse('ok')
