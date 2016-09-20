from django.test import TestCase
from .models import Project
from datetime import datetime
# Create your tests here.


class ProjectMethodsTest(TestCase):
    def test_create_simple_project(self):
        projects_starting_count = Project.objects.count()
        new_project = Project.objects.create(
            title='My new project',
            abstract='This is an example abstract for my new project.',
        )
        self.assertEqual(Project.objects.count(), projects_starting_count+1)
        self.assertEqual(new_project.title, 'My new project')
        self.assertEqual(len(new_project.abstract), 47)
        self.assertEqual(new_project.status, 0)
        self.assertEqual(new_project.date_initiated, datetime.now().date())

