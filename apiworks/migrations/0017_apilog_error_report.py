# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-09 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiworks', '0016_apiinfo_api_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='apilog',
            name='error_report',
            field=models.IntegerField(default=0, verbose_name='\u62a5\u9519'),
        ),
    ]
