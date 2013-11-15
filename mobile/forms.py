# -*- coding: utf-8 -*-
from django import forms
from punto_interes.models import PuntoInteres

class RutaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(RutaForm, self).__init__(*args, **kwargs)
        PUNTOS = map(lambda x: tuple([x.direccion,x.titulo]),PuntoInteres.objects.all())
        PUNTOS_CON = [('','Ubicación actual')]
        PUNTOS_CON.extend(PUNTOS)
        
        self.fields['inicio'] = forms.ChoiceField(label="Empezar ruta en", choices=tuple(PUNTOS_CON))
        self.fields['intermedios'] = forms.MultipleChoiceField(label="Quiero visitar", choices=tuple(PUNTOS))
        self.fields['fin'] = forms.ChoiceField(label="Finalizar ruta en", choices=tuple(PUNTOS_CON)) 
