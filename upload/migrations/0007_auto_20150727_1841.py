# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0006_auto_20150727_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='format',
            field=models.CharField(null=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='document',
            name='size',
            field=models.IntegerField(null=True),
        ),
    ]
