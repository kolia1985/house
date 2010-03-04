from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('wall.views',
    url(r'^wall_type/$', 'wall_type_list', name='wall_type_list'),
)