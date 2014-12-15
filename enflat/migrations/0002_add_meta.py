# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'CustomFlatPage'
        db.create_table('enflat_customflatpage', (
            ('meta_description', self.gf('django.db.models.fields.TextField')(default='')),
            ('meta_title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('flatpage_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['flatpages.FlatPage'], unique=True, primary_key=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal('enflat', ['CustomFlatPage'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'CustomFlatPage'
        db.delete_table('enflat_customflatpage')
    
    
    models = {
        'enflat.customflatpage': {
            'Meta': {'object_name': 'CustomFlatPage', '_ormbases': ['flatpages.FlatPage']},
            'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'meta_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        'flatpages.flatpage': {
            'Meta': {'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['enflat']
