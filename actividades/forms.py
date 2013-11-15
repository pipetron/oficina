from django import forms
from actividades.models import Reserva

class ReservaForm(forms.ModelForm):
    """
    Formulario para la reserva de actividades
    """
    fecha_inicio = forms.DateTimeField(input_formats=["%d/%m/%Y",])
    fecha_fin = forms.DateTimeField(input_formats=["%d/%m/%Y",])
    
    class Meta:
        model = Reserva
        exclude = ('docid',)