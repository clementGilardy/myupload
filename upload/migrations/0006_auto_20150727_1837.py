# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20150727_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='document',
            name='size',
            field=models.IntegerField(default=None),
        ),
    ]
