from django.test import TestCase
from django.conf import settings
from blog.models import *


class PostTestCase(TestCase):
  fixtures = ['categories.json','posts.json']
  
  def setUp(self):
    settings.ROOT_URLCONF = 'blog.urls'
      
  def testPublicPosts(self):
    self.failUnlessEqual(Post.objects.published().count(), 1)
  
  def testPosts(self):
    self.failUnlessEqual(Post.objects.count(), 3)
    
  def testPostList(self):
    response = self.client.get('/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')
  
  def testPostArchiveYear(self):
    response = self.client.get('/2007/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_archive_year.html')
  
  def testPostArchiveMonth(self):
    response = self.client.get('/2007/nov/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_archive_month.html')
  
  def testPostArchiveDay(self):
    response = self.client.get('/2007/nov/25/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_archive_day.html')
  
  def testPostDetail(self):
    post = Post.objects.get(pk=1)
    response = self.client.get('%s' % post.get_absolute_url())
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_detail.html')