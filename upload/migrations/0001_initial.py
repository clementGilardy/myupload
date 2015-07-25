# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=300)),
                ('size', models.IntegerField()),
                ('format', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(verbose_name="Date d'ajout", auto_now_add=True)),
            ],
        ),
    ]
