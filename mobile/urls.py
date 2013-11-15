from django.conf.urls.defaults import patterns

urlpatterns = patterns('mobile.views',
     (r'^$','inicio',{},'inicio_mobile'),
     (r'^galeria/$','galeria',{},'galeria_mobile'),
     (r'^galeria/galeria/(?P<galeria_id>[0-9]+)/$','galeria_detail',{},'galeria_detail_mobile'),
     (r'^rutas/$','rutas',{},'rutas_mobile'),
     (r'^contacto/$','contacto',{},'contacto_mobile'),
)