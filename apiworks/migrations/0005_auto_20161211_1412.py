# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-11 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiworks', '0004_auto_20161211_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiErrno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('errno', models.IntegerField(default=0, verbose_name='\u9519\u8bef\u7801')),
                ('errno_message', models.CharField(blank=True, max_length=200, verbose_name='\u7c7b\u578b')),
                ('param_intro', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'api_errno',
                'verbose_name': '\u9519\u8bef\u7801',
                'verbose_name_plural': '\u9519\u8bef\u7801',
            },
        ),
        migrations.CreateModel(
            name='ApiParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(blank=True, max_length=200, verbose_name='\u53c2\u6570\u540d')),
                ('param_type', models.CharField(blank=True, max_length=200, verbose_name='\u7c7b\u578b')),
                ('param_requested', models.IntegerField(default=1, verbose_name='\u5fc5\u586b')),
                ('param_location', models.IntegerField(default=1, verbose_name='\u53c2\u6570\u4f4d\u7f6e')),
                ('param_default', models.CharField(blank=True, max_length=200, verbose_name='\u9ed8\u8ba4\u503c')),
                ('param_order', models.IntegerField(default=1, verbose_name='\u6392\u5e8f')),
                ('param_description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'api_param',
                'verbose_name': '\u8bf7\u6c42\u53c2\u6570',
                'verbose_name_plural': '\u8bf7\u6c42\u53c2\u6570',
            },
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='api_method',
            field=models.IntegerField(blank=True, default=1, verbose_name='\u8bf7\u6c42\u65b9\u6cd5'),
        ),
        migrations.AddField(
            model_name='apiparam',
            name='api_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiworks.ApiInfo', verbose_name='\u6240\u5c5e\u670d\u52a1'),
        ),
        migrations.AddField(
            model_name='apierrno',
            name='api_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiworks.ApiInfo', verbose_name='\u6240\u5c5e\u670d\u52a1'),
        ),
    ]