from django.contrib import admin
from .models import Service, Affiliated

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'created')
    ordering = ('title', 'created')
    search_fields = ('title', 'subtitle')

class AffiliatedAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')
    ordering = ('name', 'created')
    search_fields = ('name',)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Affiliated, AffiliatedAdmin)