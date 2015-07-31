# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20150727_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='format',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
