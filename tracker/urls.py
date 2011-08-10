from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from settings import MEDIA_ROOT

urlpatterns = patterns('',
                       url(r'^$', 'ui.views.index'),
                       url(r'^data/', include('core.urls')),

                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':MEDIA_ROOT}),
                       url(r'^admin/', include(admin.site.urls)),
)
