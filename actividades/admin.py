from django.contrib import admin
from actividades.models import Actividad, TipoActividad, Reserva
    
admin.site.register(Actividad)   
admin.site.register(TipoActividad)
admin.site.register(Reserva)
