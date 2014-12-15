from surfblog.models import *
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'ordering', ]
    list_editable = ['ordering', ]

class BannerAdmin(admin.ModelAdmin):
	list_display = ('__unicode__','active')
	list_editable = ('active',)
	
admin.site.register(Tip)
admin.site.register(StaffMember)
admin.site.register(Partner)	
admin.site.register(Article, ArticleAdmin)
admin.site.register(Video)
admin.site.register(Banner, BannerAdmin)