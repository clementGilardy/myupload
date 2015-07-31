# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0007_auto_20150727_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='icon',
            field=models.CharField(null=True, max_length=300),
        ),
    ]
