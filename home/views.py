from django.views import generic
from models import Announcement
from projects.models import Project
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from django.utils import timezone


class HomeView(generic.ListView):
    model = Project
    template_name = 'base/home.html'
    context_object_name = 'publication_list'

    def get_queryset(self):
        return Project.objects.filter(status__exact=11).order_by('-date_published')  # Status 11 is 'Published'


class ContactView(generic.ListView):
    model = Project
    template_name = 'base/contact.html'


class ResearchView(generic.ListView):
    model = Project
    template_name = 'base/research.html'


class TechnologyView(generic.ListView):
    model = Project
    template_name = 'base/technology.html'
