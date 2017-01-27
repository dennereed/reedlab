# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
                ('charname', models.CharField(default=b'', max_length=50)),
                ('unit', models.CharField(max_length=5, null=True)),
                ('notes', models.TextField(null=True)),
                ('chartype', models.CharField(default=b'UM', max_length=5, choices=[(b'UM', b'Unordered Multistate'), (b'OM', b'Ordered Multistate'), (b'IN', b'Integer'), (b'RN', b'Real Number'), (b'TE', b'Text')])),
                ('mandatory', models.NullBooleanField(default=False)),
                ('multistatetype', models.IntegerField(default=1)),
                ('reliability', models.IntegerField(default=5)),
                ('availability', models.IntegerField(default=5)),
                ('fuzziness', models.DecimalField(default=0, max_digits=20, decimal_places=5)),
                ('fuzzinessispercent', models.NullBooleanField(default=False)),
                ('keystates', models.CharField(max_length=5, null=True)),
                ('charheading', models.IntegerField(null=True)),
                ('headinglink', models.IntegerField(null=True)),
                ('charwording', models.TextField(null=True)),
                ('charwording2', models.TextField(null=True)),
                ('unitisprefix', models.NullBooleanField(default=False)),
                ('formatstring', models.TextField(null=True)),
                ('paragraphlink', models.IntegerField(null=True)),
                ('sentencelink', models.IntegerField(null=True)),
                ('commalink', models.IntegerField(null=True)),
                ('speciallink', models.IntegerField(null=True)),
                ('specialelement', models.IntegerField(null=True)),
                ('usecomma2', models.NullBooleanField(default=False)),
                ('omitfinalcomma', models.NullBooleanField(default=False)),
                ('omitvalues', models.NullBooleanField(default=False)),
                ('emphasize', models.NullBooleanField(default=False)),
                ('omitperiod', models.NullBooleanField(default=False)),
                ('numstates', models.IntegerField(default=2, null=True)),
                ('charref', models.IntegerField(null=True)),
                ('element', models.CharField(default=b'U', max_length=4, null=True)),
                ('disabled', models.NullBooleanField(default=False)),
            ],
        ),
    ]
