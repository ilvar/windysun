import datetime

from django import template
from django.utils.safestring import mark_safe

from page_blocks.models import Block

register = template.Library()

@register.tag(name="include_block")
def do_include_block(parser, token):
    slug = token.split_contents()[1]
    nodelist = parser.parse(('endinclude',))
    parser.delete_first_token()
    return BlockNode(slug, nodelist)

class BlockNode(template.Node):
    def __init__(self, slug, nodelist):
        self.slug = slug
        self.nodelist = nodelist

    def render(self, context):
        try:
            block = Block.objects.get(slug=self.slug)
        except Block.DoesNotExist:
            output = self.nodelist.render(context)
        else:
            output = block.content
        return u'<!-- BLOCK: %s --> %s <!-- ENDBLOCK: %s -->' % (self.slug, mark_safe(output), self.slug)
