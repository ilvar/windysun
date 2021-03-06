# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Gallery'
        db.create_table('photologue_gallery', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photologue', ['Gallery'])

        # Adding M2M table for field photos on 'Gallery'
        db.create_table('photologue_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm['photologue.gallery'], null=False)),
            ('photo', models.ForeignKey(orm['photologue.photo'], null=False))
        ))
        db.create_unique('photologue_gallery_photos', ['gallery_id', 'photo_id'])

        # Adding model 'GalleryUpload'
        db.create_table('photologue_galleryupload', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('zip_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Gallery'], null=True, blank=True)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photologue', ['GalleryUpload'])

        # Adding model 'Photo'
        db.create_table('photologue_photo', (
            ('view_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('crop_from', self.gf('django.db.models.fields.CharField')(default='center', max_length=10, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photo_related', null=True, to=orm['photologue.PhotoEffect'])),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photologue', ['Photo'])

        # Adding model 'PhotoEffect'
        db.create_table('photologue_photoeffect', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('reflection_strength', self.gf('django.db.models.fields.FloatField')(default=0.59999999999999998)),
            ('brightness', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('color', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('sharpness', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('reflection_size', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('filters', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('transpose_method', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(default='#FFFFFF', max_length=7)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contrast', self.gf('django.db.models.fields.FloatField')(default=1.0)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('photologue', ['PhotoEffect'])

        # Adding model 'Watermark'
        db.create_table('photologue_watermark', (
            ('opacity', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('style', self.gf('django.db.models.fields.CharField')(default='scale', max_length=5)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('photologue', ['Watermark'])

        # Adding model 'PhotoSize'
        db.create_table('photologue_photosize', (
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('watermark', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photo_sizes', null=True, to=orm['photologue.Watermark'])),
            ('increment_count', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('effect', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='photo_sizes', null=True, to=orm['photologue.PhotoEffect'])),
            ('crop', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('height', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('width', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('upscale', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('pre_cache', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('quality', self.gf('django.db.models.fields.PositiveIntegerField')(default=70)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('photologue', ['PhotoSize'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Gallery'
        db.delete_table('photologue_gallery')

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table('photologue_gallery_photos')

        # Deleting model 'GalleryUpload'
        db.delete_table('photologue_galleryupload')

        # Deleting model 'Photo'
        db.delete_table('photologue_photo')

        # Deleting model 'PhotoEffect'
        db.delete_table('photologue_photoeffect')

        # Deleting model 'Watermark'
        db.delete_table('photologue_watermark')

        # Deleting model 'PhotoSize'
        db.delete_table('photologue_photosize')
    
    
    models = {
        'photologue.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photologue.Photo']"}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'photologue.galleryupload': {
            'Meta': {'object_name': 'GalleryUpload'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photologue.Gallery']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'photologue.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.59999999999999998'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        'photologue.photosize': {
            'Meta': {'object_name': 'PhotoSize'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.PhotoEffect']"}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment_count': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'pre_cache': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'quality': ('django.db.models.fields.PositiveIntegerField', [], {'default': '70'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'watermark': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': "orm['photologue.Watermark']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'photologue.watermark': {
            'Meta': {'object_name': 'Watermark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'opacity': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'scale'", 'max_length': '5'})
        }
    }
    
    complete_apps = ['photologue']
