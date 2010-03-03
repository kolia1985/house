from django.conf.urls.defaults import *


urlpatterns = patterns('autocomplete.views',
    url(r'^autocomplete/(?P<app_label>[^.]+).(?P<model>[^/]+)/$',
        'autocomplete', name='autocomplete'),
)
