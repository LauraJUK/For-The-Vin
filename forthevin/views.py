from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from django.template import RequestContext
from forms import UserForm



def join(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('wineries/thanks')
		else:
			print form.errors
			return Http404()
	else:
		form = UserForm()
	return render_to_response('wineries/join.html', {'form': form}, RequestContext(request))

#enter form for SelectVarietal here

def thanks(request):
	return render_to_response('wineries/thanks.html')

