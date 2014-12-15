from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from blog.models import Post

blog_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'publish',
}

sitemaps_data = {
    'blog': GenericSitemap(blog_dict, priority=0.6),
}