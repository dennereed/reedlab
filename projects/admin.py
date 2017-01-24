from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['priority', 'slug', 'title', 'theme', 'status', 'published', 'date_initiated', 'date_published']
    list_filter = ['published', 'status', 'theme', 'target_journal', 'publication_type']
    search_fields = ['id', 'slug', 'title', 'citation', 'authors', 'abstract']
    list_display_links = ['slug', 'title']
    list_editable = ['theme', 'status', 'published']

admin.site.register(Project, ProjectAdmin)