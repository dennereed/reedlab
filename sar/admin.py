from django.contrib import admin
from .models import Chapter


class ChapterAdmin(admin.ModelAdmin):
    list_display = ['chapter_number', 'stub', 'authors', 'title']
    list_display_links = ['chapter_number', 'stub']


admin.site.register(Chapter, ChapterAdmin)
