from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()
from django.views.generic import DetailView, ListView
from wineries.models import Varietal


urlpatterns = patterns('',

    (r'^$', 'forthevin.views.join'),
    
    
    (r'^wineries/', include('wineries.urls_wineries')),
    (r'^varietals/', include('wineries.urls_varietals')),  

    # Examples:   
    # url(r'^$', 'forthevin.views.home', name='home'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
)

if True:
   urlpatterns += patterns('',
       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_MEDIA_ROOT }),
   )

