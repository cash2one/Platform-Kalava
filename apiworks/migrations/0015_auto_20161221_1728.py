# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-21 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiworks', '0014_apipermission_expired_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apipermission',
            name='expired_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u5931\u6548\u65f6\u95f4'),
        ),
    ]