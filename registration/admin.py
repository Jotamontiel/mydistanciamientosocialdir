from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('birth_date', 'gender')
    list_display = ('name', 'rut')
    #ordering = ('birth_date')
    search_fields = ('user', 'nickname')

admin.site.register(Profile, ProfileAdmin)