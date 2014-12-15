from django.test import TestCase
from django.conf import settings
from blog.models import *


class CategoryTestCase(TestCase):
  fixtures = ['categories.json']
  
  def setUp(self):
    settings.ROOT_URLCONF = 'blog.urls'
  
  def testCategories(self):
    self.failUnlessEqual(Category.objects.count(), 2)
  
  def testCategoryList(self):
    response = self.client.get('/categories/')
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/category_list.html')
  
  def testCategoryDetail(self):
    category = Category.objects.get(pk=1)
    response = self.client.get('%s' % category.get_absolute_url())
    self.failUnlessEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/category_detail.html')