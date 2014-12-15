# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Tip'
        db.create_table('surfblog_tip', (
            ('text', self.gf('django.db.models.fields.TextField')(max_length=2000)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('surfblog', ['Tip'])

        # Adding model 'StaffMember'
        db.create_table('surfblog_staffmember', (
            ('is_operator', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('is_driver', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('is_teacher', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('english', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('russian', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('surfblog', ['StaffMember'])

        # Adding model 'Partner'
        db.create_table('surfblog_partner', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('surfblog', ['Partner'])

        # Adding model 'Article'
        db.create_table('surfblog_article', (
            ('text', self.gf('tinymce.models.HTMLField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('surfblog', ['Article'])

        # Adding model 'Video'
        db.create_table('surfblog_video', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('surfblog', ['Video'])

        # Adding model 'Banner'
        db.create_table('surfblog_banner', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='img/banner/flash.jpg', max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(default='http://surfersbali.com', max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('surfblog', ['Banner'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Tip'
        db.delete_table('surfblog_tip')

        # Deleting model 'StaffMember'
        db.delete_table('surfblog_staffmember')

        # Deleting model 'Partner'
        db.delete_table('surfblog_partner')

        # Deleting model 'Article'
        db.delete_table('surfblog_article')

        # Deleting model 'Video'
        db.delete_table('surfblog_video')

        # Deleting model 'Banner'
        db.delete_table('surfblog_banner')
    
    
    models = {
        'surfblog.article': {
            'Meta': {'object_name': 'Article'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'english': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_driver': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_operator': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_teacher': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'russian': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
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
