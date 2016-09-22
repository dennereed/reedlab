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
