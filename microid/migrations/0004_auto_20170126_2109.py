# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microid', '0003_auto_20170126_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='element',
            field=models.CharField(default=b'U', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='formtatstring',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='keystates',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='unit',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
