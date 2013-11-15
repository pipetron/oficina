from django.conf.urls.defaults import patterns

urlpatterns = patterns('fiestas.views',
     (r'^$','ver_fiestas',{},'ver_fiestas'),
     (r'^fiesta/(?P<fiesta_id>[0-9]+)/$','fiesta_detail',{},'fiesta_detail'),
)