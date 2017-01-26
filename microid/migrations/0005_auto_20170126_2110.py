# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microid', '0004_auto_20170126_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='charheading',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='charref',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='commalink',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='headinglink',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='paragraphlink',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='sentencelink',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='specialelement',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='speciallink',
            field=models.IntegerField(null=True),
        ),
    ]
