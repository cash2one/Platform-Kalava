# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiworks', '0008_auto_20161212_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apierrno',
            old_name='api_name',
            new_name='api',
        ),
        migrations.RenameField(
            model_name='apiparam',
            old_name='api_name',
            new_name='api',
        ),
        migrations.RenameField(
            model_name='apipermission',
            old_name='api_name',
            new_name='api',
        ),
    ]
