from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
                       url(r'(?P<index>d+)', 'core.views.data'),
)
