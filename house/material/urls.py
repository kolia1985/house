from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('material.views',
    url(r'^material/$', 'material_list', name='material_list'),
)