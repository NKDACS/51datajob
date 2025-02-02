# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkName', models.CharField(max_length=20, verbose_name='链接标题')),
                ('website', models.CharField(max_length=200, verbose_name='网址')),
                ('isPublish', models.BooleanField(default=False, verbose_name='发布')),
            ],
        ),
    ]
