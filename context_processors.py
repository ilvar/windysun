def path_bits(request):
    return {
        'path_bits': filter(lambda b:b, request.path.split('/')),
    }

def page_blocks(request):
    from page_blocks.models import Block
    from django.contrib.flatpages.models import FlatPage
    try:
        fp = FlatPage.objects.get(url=request.path)
    except FlatPage.DoesNotExist:
        fp = None
    result = {
        'page_blocks': dict(Block.objects.all().values_list('slug', 'content')),
    }
    if fp:
        result['flatpage'] = fp
    return result
