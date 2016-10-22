# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=45)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=45)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='state',
            field=models.ManyToManyField(to='base.State'),
        ),
    ]
