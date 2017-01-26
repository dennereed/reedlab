# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microid', '0002_auto_20170126_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charwording',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='charwording2',
            field=models.TextField(null=True),
        ),
    ]
