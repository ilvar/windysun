# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):
    
    def forwards(self, orm):
        from surfblog.models import StaffMember
        for sm in StaffMember.objects.all():
            sm.save()
    
    
    def backwards(self, orm):
        "Write your backwards methods here."
    
    models = {
        'surfblog.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'text': ('tinymce.models.HTMLField', [], {})
        },
        'surfblog.banner': {
            'Meta': {'object_name': 'Banner'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/banner/flash.jpg'", 'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'default': "'http://surfersbali.com'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'surfblog.partner': {
            'Meta': {'object_name': 'Partner'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'surfblog.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'big_text': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'english': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_operator': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_teacher': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'russian': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'surfblog.tip': {
            'Meta': {'object_name': 'Tip'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '2000'})
        },
        'surfblog.video': {
            'Meta': {'object_name': 'Video'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }
    
    complete_apps = ['surfblog']
