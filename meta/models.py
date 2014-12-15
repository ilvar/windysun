from django.db import models

class MetaModel(models.Model):
    meta_title = models.CharField(max_length=255, blank=True, default='')
    meta_description = models.TextField(blank=True, default='')
    meta_keywords = models.TextField(blank=True, default='')

    class Meta:
        abstract = True

