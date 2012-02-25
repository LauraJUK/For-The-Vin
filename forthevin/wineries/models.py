from django.db import models
from django.utils.functional import lazy
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.template.defaultfilters import slugify

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
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=100)
    varietals = models.ManyToManyField(Varietal)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        url =  reverse_lazy('forthevin.wineries', [self.slug])
        print url 
        return url
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
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