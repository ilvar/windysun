# -*- coding: utf-8 -*-
from django.contrib.comments.moderation import CommentModerator, moderator
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.sites.models import Site

from tagging.fields import TagField
from blog.managers import *
from photologue.models import *
from tinymce import models as tinymce_models
import tagging

from meta.models import MetaModel


class Category(models.Model):
  """ Category """
  title       = models.CharField(max_length=100)
  slug        = models.SlugField(unique=True)

  class Meta:
    verbose_name_plural = 'categories'
    db_table = 'blog_categories'
    ordering = ('title',)

  class Admin:
    pass

  def __unicode__(self):
    return '%s' % self.title

  @permalink
  def get_absolute_url(self):
    return ('blog_category_detail', None, { 'slug':self.slug })


class Post(MetaModel):
  """ Post model """
  STATUS_CHOICES = (
    (1, 'Draft'),
    (2, 'Public'),
    (3, 'Closed'),
  )
  abstr       = models.ImageField(upload_to='abstract', help_text='Image MUST be 191x127px resolution', blank=True, null=True)
  title       = models.CharField(max_length=200)
  slug        = models.SlugField(unique=True)
  author      = models.ForeignKey(User, blank=True, null=True)
  body        = tinymce_models.HTMLField()
  tease       = models.TextField(blank=True)
  status      = models.IntegerField(choices=STATUS_CHOICES, default=2)
  publish     = models.DateTimeField()
  created     = models.DateTimeField(auto_now_add=True)
  modified    = models.DateTimeField(auto_now=True)
  categories  = models.ManyToManyField(Category, blank=True)
  tags        = TagField()
  objects     = ManagerWithPublished()
  gallery     = models.ForeignKey(Gallery, blank=True, null=True)

  class Meta:
    db_table  = 'blog_posts'
    ordering  = ('-publish',)
    get_latest_by = 'publish'

  class Admin:
    list_display  = ('title', 'publish', 'status')
    list_filter   = ('publish', 'categories', 'status')
    search_fields = ('title', 'body')

  def __unicode__(self):
    return self.title

  @permalink
  def get_absolute_url(self):
      return ('blog_detail', None, {
        'year'  : self.publish.year,
        'month' : self.publish.month,
        'day'   : self.publish.day,
        'slug'  : self.slug
      })

  @permalink
  def get_short_url(self):
      return ('blog_detail_short', None, {
        'id'  : self.pk,
      })

  def get_short_title(self):
      domain = Site.objects.get_current().domain
      twit_len = 140 - len(domain) - 30
      if len(self.title) < twit_len:
          return self.title
      return self.title[0:twit_len] + '...'

  def get_share_links(self):
    site = Site.objects.get_current().domain
    data = {
        'media': settings.MEDIA_URL,
        'url': 'http://' + site + self.get_short_url(),
        'twit': self.get_short_title(),
        'title': self.title,
    }
    result = u""
    result += u"""<a title="Добавить в Twitter" href="http://twitter.com/home?status=%(twit)s:+%(url)s+%%23surfing+%%23bali" target="_blank" rel="nofollow"><img src="%(media)simg/icons/twitter.png"/></a> """ % data
    result += u"""<a title="Добавить в Facebook"  href="http://www.facebook.com/sharer.php?u=%(url)s&t=%(title)s" target="blank" rel="nofollow"><img src="%(media)simg/icons/facebook.png"/></a> """ % data
    result += u"""<a title="Добавить в ВКонтакте" href="http://vkontakte.ru/share.php?url=%(url)s&title=%(title)s" target="blank" rel="nofollow"><img src="%(media)simg/icons/vkontakte.png"/></a> """ % data
    return mark_safe(u'<span class="share">%s</span>' % result)

class PostModerator(CommentModerator):
    email_notification = True
    auto_close_field   = 'publish'
    # Close the comments after 7 days.
    close_after        = 70

#moderator.register(Post, PostModerator)
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^tinymce\.models\.HTMLField"])
add_introspection_rules([], ["^tagging\.fields\.TagField"])


from django.contrib.comments.moderation import CommentModerator, moderator
from django.contrib.sites.models import Site
from django.conf import settings

class AkismetModerator(CommentModerator):
    def check_spam(self, request, comment, key, blog_url=None, base_url=None):
        try:
            from akismet import Akismet
        except:
            return False

        if blog_url is None:
            blog_url = 'http://%s/' % Site.objects.get_current().domain

        ak = Akismet(
            key=settings.AKISMET_API_KEY,
            blog_url=blog_url
        )

        if base_url is not None:
            ak.baseurl = base_url

        if ak.verify_key():
            data = {
                'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
                'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                'referrer': request.META.get('HTTP_REFERER', ''),
                'comment_type': 'comment',
                'comment_author': comment.user_name.encode('utf-8'),
                }

            if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
                return True

        return False

    def allow(self, comment, content_object, request):
        allow = super(AkismetModerator, self).allow(comment, content_object, request)

        # change this depending on which spam provider you want to use
        spam = self.check_spam(request, comment,
            key=settings.AKISMET_API_KEY,
        )

        return not spam and allow

#try:
#    moderator.unregister(Post)
#except:
#    pass
#moderator.register(Post, AkismetModerator)

