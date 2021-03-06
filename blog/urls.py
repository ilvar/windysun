from django.conf.urls.defaults import *

from blog.feeds import BlogPostFeed

urlpatterns = patterns('blog.views',
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', view='post_detail', name= 'blog_detail'),
  url(r'^(?P<id>\d+)/$', view='post_detail_short', name='blog_detail_short'),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\w{1,2})/$', view='post_archive_day', name='blog_archive_day'),
  url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',view='post_archive_month', name='blog_archive_month'),
  url(r'^(?P<year>\d{4})/$',view='post_archive_year', name='blog_archive_year'),
  url(r'^categories/(?P<slug>[-\w]+)/$',view='category_detail', name='blog_category_detail'),
  url(r'^categories/$',view='category_list', name='blog_category_list'),
  url(r'^search/$',view='search', name='blog_search'),
  url(r'^page/(?P<page>\w)/$',view='post_list', name='blog_index_paginated'),
  url(r'^$',view='post_list', name='blog_index'),
  url(r'^tag/([^/]+)/$',view='with_tag', name='blog_with_tag_A'),
  url(r'^tag/([^/]+)/page/([^/]+)/$', view='with_tag', name='blog_with_tag'),
  url(r'^rss/$', BlogPostFeed(), name='rss'),
)
