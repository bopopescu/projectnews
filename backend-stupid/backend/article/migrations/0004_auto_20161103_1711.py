# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-03 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20161103_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_verified',
        ),
        migrations.RemoveField(
            model_name='article',
            name='status_code',
        ),
    ]
