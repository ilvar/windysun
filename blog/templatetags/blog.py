from django import template
from django.core import template_loader
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
import re
Post = models.get_model('blog', 'post')
Category = models.get_model('blog', 'category')

register = template.Library()

class LatestPosts(template.Node):
  def __init__(self, format_string, var_name):
    self.format_string = format_string
    self.var_name = var_name
  
  def render(self, context):
    posts = Post.objects.published()[:int(self.format_string)]
    context[self.var_name] = posts
    return ''

@register.tag(name='get_latest_posts')
def do_get_latest_posts(parser, token):
  """
  Gets any number of latest posts and stores them in a varable.
  
  Syntax::
  
    {% get_latest_posts [limit] as [var_name] %}
  
  Example usage::
    
    {% get_latest_posts 10 as latest_post_list %}
  """
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'(.*?) as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  format_string, var_name = m.groups()
  return LatestPosts(format_string[0], var_name)


class BlogCategories(template.Node):
  def __init__(self, var_name):
    self.var_name = var_name
  
  def render(self, context):
    categories = Category.objects.all()
    context[self.var_name] = categories
    return ''

@register.tag(name='get_blog_categories')
def do_get_blog_categories(parser, token):
  """
  Gets all blog categories.
  
  Syntax::
    
    {% get_blog_categories as [var_name] %}
  
  Example usage::
  
    {% get_blog_categories as category_list %}
  """
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  m = re.search(r'as (\w+)', arg)
  if not m:
    raise template.TemplateSyntaxError, "%s tag had invalid arguments" % tag_name
  var_name = m.groups()[0]
  return BlogCategories(var_name)


class MarkupPost(template.Node):
  def __init__(self, post):
    self.post = post
  
  
  def render(self, context):
    try:
      from BeautifulSoup import BeautifulSoup
    except ImportError:
      from beautifulsoup import BeautifulSoup
    
    soup = BeautifulSoup(context[self.post].body)
    inline_list = soup.findAll('inline')
    inline_context = {}
    
    for inline in inline_list:
      try:
        app_label, model_name = inline['type'].split('.')
        content_type = ContentType.objects.get(app_label=app_label, model=model_name)
        Model = content_type.model_class()
        
        try:
          id_list = [int(i) for i in inline['ids'].split(',')]
          object_list = Model.objects.in_bulk(id_list)
          object_list = list(object_list[int(i)] for i in id_list)
          inline_context = template.Context({ 'object_list': object_list })
          inline_template = 'inlines/%s_%s.html' % (content_type.app_label, content_type.model)
        except KeyError:
          obj = Model.objects.get(pk=inline['id'])
          inline_context = template.Context({ 'object': obj })
          inline_template = 'inlines/%s_%s.html' % (content_type.app_label, content_type.model)
      except template.TemplateDoesNotExist:
        inline_context = {'error':'Template does not exist.'}
        inline_template = 'inlines/missing.html'
      except ContentType.DoesNotExist:
        inline_context = {'error':'Content type does not exist.'}
        inline_template = 'inlines/missing.html'
      #except Model.DoesNotExist:
      #  inline_context = {'error':'Model object does not exist.'}
      #  inline_template = 'inlines/missing.html'
      except KeyError:
        inline_context = {'error':'Be sure there are both "type" and "id" attributes in the inline tag.'}
        inline_template = 'inlines/missing.html'
      except ValueError:
        inline_context = {'error':'Be sure, in the "type" attribute, to specify the app_label and model name. (e.g. jellyroll.photo)'}
        inline_template = 'inlines/missing.html'
      
      
      rendered_inline = template_loader.render_to_string(inline_template, inline_context)
      inline.replaceWith(rendered_inline)
        
    return soup

@register.tag(name='markup_post')
def do_markup_post(parser, token):
  """
  Markup post with markdown and insert inline templates.
  
  Syntax::
    {% markup_post [post_object] %}
  
  Example usage::
    {% markup_post object %}
  """
  try:
    tag_name, arg = token.contents.split(None, 1)
  except ValueError:
    raise template.TemplateSyntaxError, "%s tag requires arguments" % token.contents.split()[0]
  return MarkupPost(arg)