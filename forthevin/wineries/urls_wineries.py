from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from wineries.models import Winery, InterestedUser, Varietal


urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
                         queryset=Winery.objects.all,
                         context_object_name='wineries_list',
                         template_name='wineries/wineries.html')),            
    (r'^thanks/', 'forthevin.views.thanks'),
    (r'^(?P<slug>[-\w]+)/$',
        DetailView.as_view(
                           model=Winery,
                           template_name='wineries/wineries_pk_details.html')),

)

