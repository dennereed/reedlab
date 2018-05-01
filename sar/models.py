from django.db import models

# Create your models here.


class Chapter(models.Model):
    chapter_number = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    stub = models.CharField(null=True, blank=True, max_length=255)
    authors = models.CharField(null=True, blank=True, max_length=255)
    start_page = models.IntegerField(null=True, blank=True)
    end_page = models.IntegerField(null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    references = models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='sar/', null=True, blank=True)

    class Meta:
        ordering = ['chapter_number']


class Image(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    title = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(null=True, blank=True)
    chapter = models.ForeignKey('Chapter')
