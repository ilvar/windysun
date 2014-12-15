import haystack
import datetime
from haystack import indexes
from haystack import site
from blog.models import Post

haystack.autodiscover()

class PostIndex(indexes.SearchIndex):
    body = indexes.CharField(document=True, use_template=True)
    tease = indexes.CharField(use_template=False)
    created = indexes.DateTimeField(model_attr='created')

    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return Post.objects.filter(created__lte=datetime.datetime.now())

site.register(Post, PostIndex)

