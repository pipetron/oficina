from django.contrib import admin
from eventos.models import Evento, TipoEvento, Programa
    
admin.site.register(Evento)   
admin.site.register(TipoEvento)
admin.site.register(Programa)
