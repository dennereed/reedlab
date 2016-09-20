from django.db import models

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

JOURNAL_VOCABULARY = (
    ('Nature', 'Nature'),
    ('Science', 'Science'),
    ('PNAS', 'PNAS'),
    ('JHE', 'JHE'),
    ('AAPA', 'AAPA'),
    ('JVP', 'JVP'),
    ('PlosOne', 'PlosOne'),
    ('EvAnth', 'EvAnth'),
    ('Paleobiology', 'Paleobiology'),
)


# Create your models here.
class Project(models.Model):
    slug = models.SlugField(default='new_project')
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    status = models.IntegerField(choices=STATUS_VOCABULARY, default=0)
    priority = models.IntegerField(null=True, blank=True)
    target_journal = models.CharField(max_length=255, choices=JOURNAL_VOCABULARY, null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    date_initiated = models.DateField(auto_now_add=True)
    date_submitted = models.DateField(null=True, blank=True)
    date_revised = models.DateField(null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['priority', ]
