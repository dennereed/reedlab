# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Project
from datetime import datetime, date, timedelta
# Create your tests here.


class ProjectMethodsTest(TestCase):
    def setUp(self):
        # A simple null published project
        simple_project = Project.objects.create(
            title='My simple project',
            abstract='This is an example abstract for my new project.',
        )

        # A published project
        citation_html_string = u"""Reed, Denné N., W. Andrew Barr. 2015. Some fancy title. <i>Journal of Irreproducible
                    Results</i>. <b>35</b>:223-228."""
        Project.objects.create(
            title='My published project',
            abstract='This is an example abstract for my new project.',
            status=11,
            target_journal='EvAnth',
            authors='Denné N. Reed, W. Andrew Barr',
            date_initiated=date.today() - timedelta(120),
            date_submitted=date.today() - timedelta(90),
            date_revised=date.today() - timedelta(60),
            date_published=date.today() - timedelta(30),
            citation=citation_html_string,
            publication_type='Article',
        )

        # An old published project
        old_published_project = Project.objects.create(
            title='My old project',
            abstract='This is an example abstract for my new project.',
            date_published=date.today() - timedelta(6 * 365)
        )

        # An unpublished project
        Project.objects.create(
            title='My unpublished project',
            abstract='This is an example abstract for my new project.',
            date_published=date.today() + timedelta(1),
            publication_type='Article'
        )

    def test_create_simple_project(self):
        projects_starting_count = Project.objects.count()
        simple_project = Project.objects.get(title='My simple project')
        another_simple_project = Project.objects.create(
            title='Another simple project',
            abstract='This is an example abstract for my new project.',
        )
        self.assertEqual(Project.objects.count(), projects_starting_count+1)
        self.assertEqual(simple_project.title, 'My simple project')
        self.assertEqual(len(simple_project.abstract), 47)
        self.assertEqual(simple_project.status, 0)
        self.assertEqual(simple_project.date_initiated, datetime.now().date())

    def test_is_published_method(self):
        published_project = Project.objects.get(title='My published project')
        unpublished_project = Project.objects.get(title='My unpublished project')
        null_published_project = Project.objects.get(title='My simple project')
        self.assertTrue(published_project.is_published())
        self.assertFalse(unpublished_project.is_published())
        self.assertFalse(null_published_project.is_published())

    def test_is_recent_method(self):
        old_published_project = Project.objects.get(title='My old project')
        recent_publsihed_project = Project.objects.get(title='My published project')
        null_published_project = Project.objects.get(title='My simple project')
        self.assertTrue(old_published_project.is_published())
        self.assertFalse(old_published_project.is_recent())
        self.assertTrue(recent_publsihed_project.is_published())
        self.assertTrue(recent_publsihed_project.is_recent())
        self.assertFalse(null_published_project.is_recent())
