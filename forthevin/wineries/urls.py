from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from wineries.models import Winery, InterestedUser


urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
                         queryset=Winery.objects.all,
                         context_object_name='wineries_list',
                         template_name='wineries/index.html')),                
    (r'^thanks/', 'forthevin.views.thanks'),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
                           model=Winery,
                           template_name='wineries/detail.html')),

)

