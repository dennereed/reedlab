# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField()),
                ('status', models.IntegerField(default=0, max_length=255, choices=[(b'inchoate', 0), (b'brainstorm', 1), (b'data collection', 2), (b'preliminary analysis', 3), (b'outline', 4)])),
                ('target_journal', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Nature', b'Nature'), (b'Science', b'Science'), (b'PNAS', b'PNAS'), (b'JHE', b'JHE'), (b'AAPA', b'AAPA'), (b'JVP', b'JVP'), (b'PlosOne', b'PlosOne'), (b'EvAnth', b'EvAnth'), (b'Paleobiology', b'Paleobiology')])),
                ('authors', models.TextField(null=True, blank=True)),
                ('date_initiated', models.DateField(auto_now_add=True)),
                ('date_submitted', models.DateField(null=True, blank=True)),
                ('date_revised', models.DateField(null=True, blank=True)),
                ('date_published', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
