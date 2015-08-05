# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_auto_20150801_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docContains',
        ),
        migrations.AddField(
            model_name='document',
            name='docContains',
            field=models.ManyToManyField(to='upload.Document', related_name='docContains_rel_+', null=True),
        ),
    ]
