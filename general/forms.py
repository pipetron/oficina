from django import forms
from general.models import Contacto

class ContactoForm(forms.ModelForm):
    """
    Formulario para contacto
    """
    
    class Meta:
        model = Contacto
        exclude = ('fecha',)