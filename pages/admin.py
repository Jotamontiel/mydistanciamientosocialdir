from django.contrib import admin
from .models import PageVideo, PageImage, Page

# Register your models here.
class PageVideoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

class PageImageAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(PageVideo, PageVideoAdmin)
admin.site.register(PageImage, PageImageAdmin)
admin.site.register(Page, PageAdmin)