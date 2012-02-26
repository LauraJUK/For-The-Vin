from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import RequestContext
from forthevin.wineries.models import *
from django.db.models import Count

def join(request, color=None, slug=None):
    data = {}
#    data['colors'] = Color.objects.order_by('name')
#    data['varietals'] = Varietal.objects.annotate(color_count=Count('color')).order_by('-color')
    data['colors'] = Color.objects.annotate(varietal_count=Count('varietal')).order_by('-varietal_count')
    return render_to_response('wineries/join.html', data, context_instance=RequestContext(request))

def wineries(request, color=None, slug=None):
    data = {}
    show_wineries = False
    data['colors'] = Color.objects.annotate(varietal_count=Count('varietal')).order_by('-varietal_count')
    if color: #if color has been selected (in url), we want to show varietals of that color
        c = Color.objects.get(name=color) #c is a model object; color is a string
        data['color'] = c
        varietals = Varietal.objects.filter(color=c)
        data['varietals'] = varietals
        show_wineries = True
    else: #we want to show all colors and varietals
        varietals = Varietal.objects.all()
        data['varietals'] = varietals
    
    if slug: #if we have a slug, we want wineries for a specific varietal
        selected_varietal = Varietal.objects.get(slug=slug) #varietal matching the given slug
        wineries = selected_varietal.winery_set.all()
        data['wineries'] = wineries
        data['varietal'] = selected_varietal
    else: # no slug, so we want all wineries for a given color
        winery_set = set([])
        for varietal in varietals:
            varietal_winery_set = varietal.winery_set.all()
            for winery in varietal_winery_set:
                winery_set.add(winery)
        data['wineries'] = winery_set
        data['selected_varietal'] = None
    data['show_wineries'] = show_wineries
    return render_to_response('wineries/varietals_pk_wineries.html', data, context_instance=RequestContext(request))   