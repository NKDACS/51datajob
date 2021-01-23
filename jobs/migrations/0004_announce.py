# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_link_orderid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annTitle', models.CharField(max_length=20, verbose_name='公告标题')),
                ('annInfo', models.TextField(max_length=500, verbose_name='公告内容')),
                ('annLink', models.CharField(max_length=200, verbose_name='详情链接(若无请不填)')),
                ('orderID', models.IntegerField(verbose_name='顺序ID')),
                ('isPublish', models.BooleanField(default=False, verbose_name='发布')),
            ],
        ),
    ]
