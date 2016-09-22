from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['priority', 'slug', 'title', 'status', 'date_initiated', 'date_published']
    list_filter = ['status']
    search_fields = ['id', 'slug', 'title']
    list_display_links = ['slug', 'title']

admin.site.register(Project, ProjectAdmin)