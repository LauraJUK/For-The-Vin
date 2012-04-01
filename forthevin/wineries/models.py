from django.db import models
from django.utils.functional import lazy
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.template.defaultfilters import slugify
from helpers import get_lat_lng ## Calling helper file

reverse_lazy = lambda name=None, *args : lazy(reverse, str)(name, args=args)

class Color(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
    
class Varietal(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    color = models.ForeignKey(Color, blank=True, null=True)
                    
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Winery(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=250, null=True, blank=True)
    zip = models.CharField(max_length=20)
    country = models.CharField(blank=True, max_length=100)
    latlng = models.CharField(blank=True, max_length=100)
    varietals = models.ManyToManyField(Varietal)
    slug = models.SlugField()
    website = models.CharField(blank=True, null=True, max_length=256)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        url =  reverse_lazy('forthevin.wineries', [self.slug])
        print url 
        return url
    
#    def save(self, *args, **kwargs):
#        if not self.slug:
#            self.slug = slugify(self.name)
#        super(Winery, self).save(*args, **kwargs)
        
## Geocode using full address
    def _get_full_address(self):
        return u'%s %s %s %s %s %s' % (self.address1, self.address2, self.city, self.state, self.country, self.zip)
    full_address = property(_get_full_address)

    ## Geocode by just using zip and country name (faster and more reliable)
    def _get_geo_address(self):
        return '%s %s' %(self.country, self.zip)
    geo_address = property(_get_geo_address)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.latlng:
            if self.zip and self.country:
                location = self.geo_address
                self.latlng = get_lat_lng(location)
            else:
                location = '+'.join(filter(None, (self.address1, self.address2, self.city, self.state, self.country)))
                self.latlng = get_lat_lng(location)
        super(Winery, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ['name']

class Wine(models.Model):
    name = models.CharField(max_length=100)
    winery = models.ForeignKey(Winery, related_name='wines')
    varietal = models.ForeignKey(Varietal)
    year = models.IntegerField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']
        
class InterestedUser(models.Model):
    email = models.EmailField(max_length=100)
    comments = models.CharField(max_length=500)
    def __unicode__(self):
        return self.email
    class Meta:
        ordering = ['email']