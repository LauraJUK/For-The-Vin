# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Winery'
        db.create_table('wineries_winery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('wineries', ['Winery'])

        # Adding model 'Varietal'
        db.create_table('wineries_varietal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('wineries', ['Varietal'])

        # Adding model 'Wine'
        db.create_table('wineries_wine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('winery', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wines', to=orm['wineries.Winery'])),
            ('varietal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wineries.Varietal'])),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('wineries', ['Wine'])

        # Adding model 'User'
        db.create_table('wineries_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('wineries', ['User'])


    def backwards(self, orm):
        
        # Deleting model 'Winery'
        db.delete_table('wineries_winery')

        # Deleting model 'Varietal'
        db.delete_table('wineries_varietal')

        # Deleting model 'Wine'
        db.delete_table('wineries_wine')

        # Deleting model 'User'
        db.delete_table('wineries_user')


    models = {
        'wineries.user': {
            'Meta': {'object_name': 'User'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wineries.varietal': {
            'Meta': {'ordering': "['name']", 'object_name': 'Varietal'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wineries']
