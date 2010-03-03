from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
   #admin
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('core.urls')),
    (r'^', include('registration.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/'), 'serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True, }),
    )
