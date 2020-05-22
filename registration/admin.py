from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('birth_date', 'gender')
    list_display = ('rut', 'birth_date', 'gender')
    #ordering = ('birth_date')
    search_fields = ('user', 'rut', 'birth_date', 'gender')

admin.site.register(Profile, ProfileAdmin)