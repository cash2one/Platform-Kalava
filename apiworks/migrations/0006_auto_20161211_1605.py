# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiworks', '0005_auto_20161211_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiinfo',
            options={'verbose_name': 'API\u7ba1\u7406', 'verbose_name_plural': 'API\u7ba1\u7406'},
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='reply_sample',
            field=models.TextField(null=True, verbose_name='JSON\u8fd4\u56de\u793a\u4f8b'),
        ),
        migrations.AddField(
            model_name='apiinfo',
            name='request_sample',
            field=models.TextField(null=True, verbose_name='\u8bf7\u6c42\u793a\u4f8b'),
        ),
    ]