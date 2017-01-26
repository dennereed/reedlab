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
                ('unit', models.CharField(max_length=5)),
                ('notes', models.TextField()),
                ('chartype', models.CharField(default=b'UM', max_length=5, choices=[(b'UM', b'Unordered Multistate'), (b'OM', b'Ordered Multistate'), (b'IN', b'Integer'), (b'RN', b'Real Number'), (b'TE', b'Text')])),
                ('mandatory', models.BooleanField(default=False)),
                ('multistatetype', models.IntegerField(default=1)),
                ('reliability', models.IntegerField(default=5)),
                ('availability', models.IntegerField(default=5)),
                ('fuzziness', models.DecimalField(default=0, max_digits=20, decimal_places=5)),
                ('fuzzinessispercent', models.BooleanField(default=False)),
                ('keystates', models.CharField(max_length=5)),
                ('charheading', models.IntegerField()),
                ('headinglink', models.IntegerField()),
                ('charwording', models.TextField()),
                ('charwording2', models.TextField()),
                ('unitisprefix', models.BooleanField(default=False)),
                ('formtatstring', models.TextField()),
                ('paragraphlink', models.IntegerField()),
                ('sentencelink', models.IntegerField()),
                ('commalink', models.IntegerField()),
                ('speciallink', models.IntegerField()),
                ('specialelement', models.IntegerField()),
                ('usecomma2', models.BooleanField(default=False)),
                ('omitfinalcomma', models.BooleanField(default=False)),
                ('omitvalues', models.BooleanField(default=False)),
                ('emphasize', models.BooleanField(default=False)),
                ('omitperiod', models.BooleanField(default=False)),
                ('numstates', models.IntegerField(default=2)),
                ('charref', models.IntegerField()),
                ('element', models.CharField(default=b'U', max_length=4)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
    ]
