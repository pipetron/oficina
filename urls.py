from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from os import path

BASEDIR = path.dirname(path.abspath(__file__))
admin.autodiscover()

urlpatterns = patterns('',
     (r'^admin/jsi18n/$', 'django.views.i18n.javascript_catalog'),
     url(r'^admin/', include(admin.site.urls)),
     (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': path.join(BASEDIR, 'media')}),
     
     (r'^$','general.views.inicio',{},'pagina_inicio'),
     (r'^contacto/','general.views.contacto',{},'contacto'),
     (r'^documentos/descargar/(?P<id>.+)/$','general.views.descargar_documento',{},'descargar_documento'),
     (r'^documentos/','general.views.documentos',{},'documentos'),
     (r'^mobile/', include('mobile.urls')),
     (r'^fiestas/', include('fiestas.urls')),
     (r'^eventos/', include('eventos.urls')),
     (r'^actividades/', include('actividades.urls')),
     (r'^tinymce/', include('tinymce.urls')),
     (r'^galerias/', include('photologue.urls')),
     (r'^olvera/', include('punto_interes.urls')),
)
