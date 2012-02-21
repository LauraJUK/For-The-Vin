# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Color'
        db.create_table('wineries_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('wineries', ['Color'])

        # Renaming column for 'Varietal.color' to match new field type.
        db.rename_column('wineries_varietal', 'color', 'color_id')
        # Changing field 'Varietal.color'
        db.alter_column('wineries_varietal', 'color_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wineries.Color']))

        # Adding index on 'Varietal', fields ['color']
        db.create_index('wineries_varietal', ['color_id'])


    def backwards(self, orm):
        
        # Removing index on 'Varietal', fields ['color']
        db.delete_index('wineries_varietal', ['color_id'])

        # Deleting model 'Color'
        db.delete_table('wineries_color')

        # Renaming column for 'Varietal.color' to match new field type.
        db.rename_column('wineries_varietal', 'color_id', 'color')
        # Changing field 'Varietal.color'
        db.alter_column('wineries_varietal', 'color', self.gf('django.db.models.fields.IntegerField')())


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
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wineries.Color']"}),
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
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'varietals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wineries.Varietal']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wineries']
