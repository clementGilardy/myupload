# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0011_auto_20150803_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docContains',
        ),
        migrations.AddField(
            model_name='document',
            name='docContains',
            field=models.ForeignKey(null=True, to='upload.Document'),
        ),
    ]
