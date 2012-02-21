from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from wineries.models import Varietal
from django.shortcuts import get_object_or_404


urlpatterns = patterns('forthevin.wineries.views',
    (r'^(?P<color>\w+)/$', 'wineries'),
    (r'^(?P<color>\w+)/(?P<slug>[-\w]+)/$', 'wineries'),
    (r'^$', 'wineries'),
#    (r'^$',
#        ListView.as_view(
#                         queryset=Varietal.objects.all(),
#                         template_name="wineries/varietals.html",
#                         context_object_name='varietals_list',
#                        )),            
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
                           model=Varietal,
                           template_name='wineries/varietals_pk_wineries.html')),

)



