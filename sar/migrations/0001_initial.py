# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(null=True, blank=True)),
                ('stub', models.CharField(max_length=255, null=True, blank=True)),
                ('authors', models.CharField(max_length=255, null=True, blank=True)),
                ('start_page', models.IntegerField(null=True, blank=True)),
                ('end_page', models.IntegerField(null=True, blank=True)),
                ('abstract', models.TextField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
                ('references', models.TextField(null=True, blank=True)),
                ('pdf', models.FileField(upload_to=b'sar/')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('chapter', models.ForeignKey(to='sar.Chapter')),
            ],
        ),
    ]
