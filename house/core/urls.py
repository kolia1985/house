from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('core.views',
    url(r'^$', 'home', name='home'),
    url(r'^project/(?P<project_slug>[^/]+)/$', 'project', \
        name='project'),
    url(r'^floor/(?P<id>\d+)/$', 'floor', \
        name='floor'),
)
