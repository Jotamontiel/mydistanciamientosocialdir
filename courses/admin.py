from django.contrib import admin
from .models import Location, Modality, Category, Course

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('address', 'name', 'created')
    ordering = ('address', 'created')
    search_fields = ('address', 'name')

class ModalityAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'state', 'period', 'created')
    ordering = ('name', 'period', 'created')
    search_fields = ('name', 'state', 'period')
    list_filter = ('location__address',)
    
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created')
    ordering = ('name', 'created')
    search_fields = ('name',)
    
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'initials', 'managers', 'course_modality', 'category', 'created')
    ordering = ('name', 'initials', 'created')
    search_fields = ('name', 'initials', 'managers')
    list_filter = ('category__name', 'modality__name')

    def course_modality(self, obj):
        return ", ".join([c.name for c in obj.modality.all().order_by("name")])
    course_modality.short_description = "Modalidades"

admin.site.register(Location, LocationAdmin)
admin.site.register(Modality, ModalityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)