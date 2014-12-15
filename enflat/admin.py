# setup flatpages to use tiny_mce
from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.utils.translation import ugettext_lazy as _

from models import CustomFlatPage

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = CustomFlatPage

class FlatPageAdmin(FlatPageAdminOld):
    form = FlatPageForm

    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
        (_('META'), {'classes': ('collapse',), 'fields': ('meta_title', 'meta_description', 'meta_keywords')}),
    )

# We have to unregister it, and then reregister
# admin.site.unregister(FlatPage)
admin.site.register(CustomFlatPage, FlatPageAdmin)
