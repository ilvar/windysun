from django.db import models

class Block(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title