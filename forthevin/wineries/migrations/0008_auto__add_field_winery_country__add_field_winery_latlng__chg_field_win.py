# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Winery.country'
        db.add_column('wineries_winery', 'country', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Winery.latlng'
        db.add_column('wineries_winery', 'latlng', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Changing field 'Winery.zip'
        db.alter_column('wineries_winery', 'zip', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Changing field 'Winery.address2'
        db.alter_column('wineries_winery', 'address2', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Winery.state'
        db.alter_column('wineries_winery', 'state', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Winery.country'
        db.delete_column('wineries_winery', 'country')

        # Deleting field 'Winery.latlng'
        db.delete_column('wineries_winery', 'latlng')

        # Changing field 'Winery.zip'
        db.alter_column('wineries_winery', 'zip', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Winery.address2'
        db.alter_column('wineries_winery', 'address2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Winery.state'
        db.alter_column('wineries_winery', 'state', self.gf('django.db.models.fields.CharField')(default=0, max_length=20))


    models = {
        'wineries.color': {
            'Meta': {'object_name': 'Color'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'wineries.interesteduser': {
            'Meta': {'ordering': "['email']", 'object_name': 'InterestedUser'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wineries.varietal': {
            'Meta': {'ordering': "['name']", 'object_name': 'Varietal'},
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wineries.Color']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'wineries.wine': {
            'Meta': {'ordering': "['name']", 'object_name': 'Wine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'varietal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wineries.Varietal']"}),
            'winery': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wines'", 'to': "orm['wineries.Winery']"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'wineries.winery': {
            'Meta': {'ordering': "['name']", 'object_name': 'Winery'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latlng': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'varietals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wineries.Varietal']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['wineries']
