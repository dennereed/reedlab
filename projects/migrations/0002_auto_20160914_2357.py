# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=b'new_project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'inchoate'), (1, b'brainstorm'), (2, b'data collection'), (3, b'preliminary analysis'), (4, b'outline'), (5, b'first draft'), (6, b'rough draft'), (7, b'friendly review'), (8, b'fiendly revision'), (9, b'submitted'), (10, b'revised'), (11, b'published')]),
        ),
    ]
