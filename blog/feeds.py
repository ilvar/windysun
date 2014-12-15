from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed as FeedView

from blog.models import Post

class BlogPostFeed(FeedView):
  _site = Site.objects.get_current()
  title = '%s feed' % _site.name
  link = '/posts/'
  description = '%s posts feed.' % _site.name

  def items(self):
    return Post.objects.published()[:10]
    
  def item_pubdate(self, item):
    return item.publish