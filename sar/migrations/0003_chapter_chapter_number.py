# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sar', '0002_auto_20180501_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
