from django.conf.urls.defaults import patterns

urlpatterns = patterns('punto_interes.views',
     (r'^$','olvera',{},'olvera'),
     (r'^punto-interes/(?P<punto_interes_id>[0-9]+)/$','punto_interes',{},'punto_interes'),
)