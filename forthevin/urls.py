from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^$', 'forthevin.views.join'),
    
#    Can I go directly to a template?
    
    (r'^wineries/', include('wineries.urls')),
    
    # url(r'^forthevin/', include('forthevin.urls')),
        # (r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),

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

