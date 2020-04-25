from django.contrib import admin
from .models import Service, Associated

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'created')
    ordering = ('title', 'created')
    search_fields = ('title', 'subtitle')

class AssociatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'created')
    ordering = ('title', 'created')
    search_fields = ('title',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Associated, AssociatedAdmin)