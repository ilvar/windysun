from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.template import RequestContext

from surfblog.models import *
from blog.models import *
from tagging.models import Tag, TaggedItem


def index(request):
    try:
        random_tip = Tip.objects.order_by("?")[0]
    except IndexError:
        random_tip = None
    post_all = Post.objects.published()[0:10]
    try:
        banners = Banner.objects.filter(active=True)
    except Banner.DoesNotExist:
        banners = []
    sample_size = ":%s" % getattr(settings, 'GALLERY_SAMPLE_SIZE', 1)
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def about(request):
    try:
        flatpage = FlatPage.objects.get(url=request.path)
    except FlatPage.DoesNotExist:
        pass
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))

def team(request):
    teacher_list = StaffMember.objects.filter(is_teacher = 'True')
    operator_list = StaffMember.objects.filter(is_operator = 'True')
    driver_list = StaffMember.objects.filter(is_driver = 'True')
    return render_to_response('team.html', locals(), context_instance=RequestContext(request))

def team_member(request, slug):
    member = get_object_or_404(StaffMember, slug=slug)
    return render_to_response('team_member.html', {'member': member}, context_instance=RequestContext(request))


def contacts(request):
    return render_to_response('contacts.html', locals(), context_instance=RequestContext(request))

def partners(request):
    partner_list = Partner.objects.all()
    return render_to_response('partners.html', locals(), context_instance=RequestContext(request))

def useful(request, offset):
    article_list = Article.objects.exclude(slug = offset).order_by('name', 'ordering')
    current_article = Article.objects.get( slug = offset )
    return render_to_response('useful.html', locals(), context_instance=RequestContext(request))

def useful_index(request):
    article_list = Article.objects.exclude(id = '1').order_by('name', 'ordering')
    current_article = Article.objects.get( id = '1' )
    return render_to_response('useful.html', locals(), context_instance=RequestContext(request))

def prices(request):
    return render_to_response('prices.html', locals(), context_instance=RequestContext(request))

def video(request):
    video_list = Video.objects.all()
    video_list = video_list.order_by("-id")
    return render_to_response('video.html', locals(), context_instance=RequestContext(request))

def video_with_tag(request, tag, object_id=None, page=1):
    query_tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(Video, query_tag)
    entries = entries.order_by('-id')
    return render_to_response("video_with_tag.html", dict(tag=tag, entries=entries), context_instance=RequestContext(request))

def reservation(request):
    subject = request.GET.get('sender_name', '')
    sender = request.GET.get('sender_email', '')
    message = request.GET.get('sender_info', '')
    date = request.GET.get('sender_date', '')
    if subject:
        subject = subject + ', ' + date
        success = send_mail(subject, message, sender, ['windysun@surfersbali.com',], fail_silently=True)
    return render_to_response('reservation.html', locals(), context_instance=RequestContext(request))
