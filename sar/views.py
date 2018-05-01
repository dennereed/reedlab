from django.shortcuts import render
from django.views import generic
from .models import Chapter


class TableOfContentsView(generic.ListView):
    model = Chapter
    template_name = 'sar/toc.html'
    context_object_name = 'chapter_list'
