# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='disabled',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='emphasize',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='fuzzinessispercent',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='mandatory',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='numstates',
            field=models.IntegerField(default=2, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='omitfinalcomma',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='omitperiod',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='omitvalues',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='unitisprefix',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='character',
            name='usecomma2',
            field=models.NullBooleanField(default=False),
        ),
    ]
