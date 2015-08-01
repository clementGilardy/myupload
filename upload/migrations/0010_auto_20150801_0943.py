# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0009_document_doccontains'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='realPath',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
