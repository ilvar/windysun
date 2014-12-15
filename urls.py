from django.conf.urls.defaults import *
from windy.views import *
from django.views.static import serve
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    # Example:
    # (r'^villacatalog/', include('villacatalog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^video/$', video),
    (r'^video/tag/([^/]+)/$', video_with_tag),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^photologue/', include('photologue.urls')),
    # (r'^admin/(.*)', admin.site.root),
    (r'^search/', include('haystack.urls')),
    (r'^reservation/$', reservation),
    (r'^about/team/$', team),
    url(r'^about/team/(.+)/$', team_member, name="team_member"),
    (r'^about/contacts/$', contacts),
    (r'^blog/', include ('windy.blog.urls')),
    (r'^useful/$', useful_index),
    (r'^useful/([^/]+)/$', useful),
    (r'^contacts/$', contacts),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^partners/$', partners),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^robots.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt'}),
    (r'^$', index),

)

from sitemaps import sitemaps_data
urlpatterns += patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps_data}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps_data}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^%s/(?P<path>.*)$' % settings.ADMIN_MEDIA_PREFIX[1:-1], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '../media-admin/', 'show_indexes': True}),
    )