from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from wineries.models import Varietal


urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
                         queryset=Varietal.objects.all,
                         context_object_name='varietals_list',
                         template_name='wineries/varietals.html')),            
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
                           model=Varietal,
                           template_name='wineries/varietals_pk_wineries.html')),

)

