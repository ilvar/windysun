from django.db import models
from django import forms

from tinymce import models as tinymce_models
from tagging.fields import TagField
from meta.models import MetaModel
from photologue.models import Gallery

import pytils

class Tip (models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    def __unicode__(self): return self.name

class StaffMember (models.Model):
    avatar = models.ImageField(upload_to='avatars',help_text='Image MUST be 130x129px resolution')
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    text = models.TextField()

    slug = models.SlugField(null=True, editable=False)
    big_text = tinymce_models.HTMLField(blank=True, null=True)
    gallery = models.ForeignKey(Gallery, blank=True, null=True, limit_choices_to={'is_public': False})

    is_driver = models.BooleanField()
    is_teacher = models.BooleanField()
    is_operator = models.BooleanField()
    english = models.BooleanField()
    russian = models.BooleanField()

    def __unicode__(self): return self.name

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name)
        super(StaffMember, self).save(*args, **kwargs)

class Partner (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='partners',help_text='Image MUST be 219x104px resolution')
    text = models.TextField()
    link = models.URLField(verify_exists = False)
    def __unicode__(self): return self.name

class Article (MetaModel):
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True)
    text = tinymce_models.HTMLField()

    ordering = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordering', 'name']

    def __unicode__(self): return self.name

class Video (models.Model):
    name = models.CharField(max_length=60)
    code = models.TextField()
    text = models.TextField()
    tags = TagField()

    def __unicode__(self): return self.name

class Banner (models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='img/banner/', default="img/banner/flash.jpg")
    active = models.BooleanField()
    link = models.URLField(verify_exists = False, default="http://surfersbali.com")
    def __unicode__(self): return self.name