# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_document_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='autor',
            new_name='author',
        ),
    ]
