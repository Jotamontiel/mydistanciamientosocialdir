from django.contrib import admin
from .models import Capsule

# Register your models here.
class CapsuleAdmin(admin.ModelAdmin):
    readonly_fields = ('lat', 'lng')
    list_display = ('name', 'nickname', 'lat', 'lng')
    #ordering = ('birth_date')
    search_fields = ('name', 'nickname', 'father_last_name', 'mother_last_name')

admin.site.register(Capsule, CapsuleAdmin)