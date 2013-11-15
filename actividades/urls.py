from django.conf.urls.defaults import patterns

urlpatterns = patterns('actividades.views',
     (r'^$','actividades',{},'actividades'),
     (r'^actividad/(?P<actividad_id>[0-9]+)/$','actividad_detail',{},'actividad_detail'),
     (r'^reservar/','reservar',{},'reservar_actividad'),
)