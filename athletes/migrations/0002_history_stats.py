# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '__first__'),
        ('sports', '0003_auto_20161012_1906'),
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.CharField(max_length=45)),
                ('evaluations', models.ForeignKey(to='administrator.Evaluations')),
                ('history', models.ForeignKey(to='athletes.Athlete_history')),
                ('profile', models.ForeignKey(to='athletes.Athlete_profile')),
                ('sport', models.ForeignKey(to='sports.Sport')),
            ],
            options={
                'verbose_name_plural': 'History_Stats',
            },
        ),
    ]
