from general.models import SeccionPie

def secciones(request):
    parametros = {}
    parametros['secciones'] = SeccionPie.objects.filter(visible=True)[0:4]
    
    return parametros