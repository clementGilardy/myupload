# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20150727_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
