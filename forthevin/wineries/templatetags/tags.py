'''
Created on Feb 20, 2012

@author: laurajohnson
'''
from django import template
from django.core.urlresolvers import reverse


register = template.Library()

## tags.py
@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''