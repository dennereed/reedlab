from django.db import models
from datetime import datetime, timedelta, date

STATUS_VOCABULARY = (
    (0, 'inchoate'),
    (1, 'brainstorm'),
    (2, 'data collection'),
    (3, 'preliminary analysis'),
    (4, 'outline'),
    (5, 'first draft'),
    (6, 'rough draft'),
    (7, 'friendly review'),
    (8, 'fiendly revision'),
    (9, 'submitted'),
    (10, 'revised'),
    (11, 'published'),
)

THEME_VOCABULARY = (
    ('Amboseli', 'Amboseli'),
    ('Ethiopia', 'Ethiopia'),
    ('Morocco', 'Morocco'),
    ('PaleoCore', 'PaleoCore'),
    ('Serengeti Mara', 'Serengeti Mara'),
    ('Species', 'Species'),
)


JOURNAL_VOCABULARY = (
    ('Nature', 'Nature'),
    ('Science', 'Science'),
    ('PNAS', 'PNAS'),
    ('JHE', 'JHE'),
    ('AAPA', 'AAPA'),
    ('Journal of Biogeography', 'Journal of Biogeography'),
    ('JVP', 'JVP'),
    ('PlosOne', 'PlosOne'),
    ('EvAnth', 'EvAnth'),
    ('Paleobiology', 'Paleobiology'),
    ('JAS', 'JAS'),
    ('Historical Biology', 'Historical Biology'),

)

PUBLICATION_TYPES = (
    ('Abstract', 'Abstract'),
    ('Article', 'Article'),
    ('Book', 'Book'),
    ('Book Chapter', 'Book Chapter'),
    ('Edited Book', 'Edited Book'),
)


# Create your models here.
class Project(models.Model):
    slug = models.SlugField(default='new_project')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    theme = models.CharField(max_length=200, null=True, blank=True, choices=THEME_VOCABULARY)
    status = models.IntegerField(choices=STATUS_VOCABULARY, default=0)
    priority = models.IntegerField(null=True, blank=True)
    target_journal = models.CharField(max_length=255, choices=JOURNAL_VOCABULARY, null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    date_initiated = models.DateField(auto_now_add=True)
    date_submitted = models.DateField(null=True, blank=True)
    date_revised = models.DateField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    citation = models.TextField(null=True, blank=True)
    publication_type = models.CharField(max_length=255, null=True, blank=True, choices=PUBLICATION_TYPES)
    pdf = models.FileField(upload_to="projects/pdfs", null=True, blank=True)
    journal_link = models.URLField(null=True, blank=True)
    selected_pub = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def is_published(self):
        result = False
        if self.status == 11:
            result = True
        return result

    def is_recent(self):
        five_years_ago = date.today() - timedelta(10*365)  # timedelta in days
        result = False
        if self.is_published() and self.date_published >= five_years_ago:
            result = True
        return result

    class Meta:
        ordering = ['priority', ]
