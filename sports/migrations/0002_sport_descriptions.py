# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='descriptions',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
