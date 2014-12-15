# setup flatpages to use tiny_mce
from django.contrib import admin

from models import Block

class BlockAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['title', 'slug',]

admin.site.register(Block, BlockAdmin)
