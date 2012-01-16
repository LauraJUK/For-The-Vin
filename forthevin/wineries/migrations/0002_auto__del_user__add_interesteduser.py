# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'User'
        db.delete_table('wineries_user')

        # Adding model 'InterestedUser'
        db.create_table('wineries_interesteduser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('wineries', ['InterestedUser'])

        # Adding M2M table for field varietals on 'Winery'
        db.create_table('wineries_winery_varietals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('winery', models.ForeignKey(orm['wineries.winery'], null=False)),
            ('varietal', models.ForeignKey(orm['wineries.varietal'], null=False))
        ))
        db.create_unique('wineries_winery_varietals', ['winery_id', 'varietal_id'])


    def backwards(self, orm):
        
        # Adding model 'User'
        db.create_table('wineries_user', (
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('wineries', ['User'])

        # Deleting model 'InterestedUser'
        db.delete_table('wineries_interesteduser')

        # Removing M2M table for field varietals on 'Winery'
        db.delete_table('wineries_winery_varietals')


    models = {
        'wineries.interesteduser': {
            'Meta': {'ordering': "['email']", 'object_name': 'InterestedUser'},
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
            'varietals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wineries.Varietal']", 'symmetrical': 'False'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['wineries']
