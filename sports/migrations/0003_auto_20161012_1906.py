# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_sport_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='activate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sport',
            name='gender',
            field=models.CharField(default=datetime.datetime(2016, 10, 12, 19, 6, 53, 26667, tzinfo=utc), max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='position_act',
            field=models.BooleanField(default=True),
        ),
    ]
