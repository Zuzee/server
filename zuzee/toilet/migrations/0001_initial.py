# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Toilet'
        db.create_table('toilet_toilet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('public', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('for_men', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('for_women', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('for_handicapped', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('toilet', ['Toilet'])


    def backwards(self, orm):
        # Deleting model 'Toilet'
        db.delete_table('toilet_toilet')


    models = {
        'toilet.toilet': {
            'Meta': {'object_name': 'Toilet'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'for_handicapped': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'for_men': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'for_women': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['toilet']