from django.conf.urls.defaults import patterns

urlpatterns = patterns('eventos.views',
     (r'^$','eventos',{},'eventos'),
     (r'^evento/(?P<evento_id>[0-9]+)/$','evento_detail',{},'evento_detail'),
)