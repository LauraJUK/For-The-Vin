## Helper file to geocode address using Google Geocoder
## From http://seanlin.me/2011/11/17/automate-geocoding-in-django-model/

import urllib, urllib2
import json as simplejson
from django.utils.encoding import smart_str

def get_lat_lng(location):
    
    # Reference: http://djangosnippets.org/snippets/293/
    
    location = urllib.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib2.urlopen(url).read() 
    result = simplejson.loads(response)
    if result['status'] == 'OK':
        lat = str(result['results'][0]['geometry']['location']['lat'])
        lng = str(result['results'][0]['geometry']['location']['lng'])
        return '%s,%s' % (lat, lng)
    else:
        return ''