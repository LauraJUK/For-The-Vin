from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from wineries.models import Varietal
from django.shortcuts import get_object_or_404


class VarietalListView(ListView):

    context_object_name = "varietals_list"
    template_name = "wineries/varietals_pk_wineries.html"

    def get_queryset(self):
        self.varietal = get_object_or_404(Varietal, slug__iexact=self.kwargs['slug'])
        return Varietal.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(VarietalListView, self).get_context_data(**kwargs)
        context['varietal'] = self.varietal
        return context
    
urlpatterns = patterns('',
    (r'^(?P<slug>[-\w]+)/$', VarietalListView.as_view()),
    (r'^$',
        ListView.as_view(
                         queryset=Varietal.objects.all(),
                         template_name="wineries/varietals.html",
                         context_object_name='varietals_list',
                        )),            
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
                           model=Varietal,
                           template_name='wineries/varietals_pk_wineries.html')),



)



