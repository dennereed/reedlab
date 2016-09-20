# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160914_2357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
