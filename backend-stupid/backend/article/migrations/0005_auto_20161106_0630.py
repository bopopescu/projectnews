# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-06 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20161103_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
    ]