# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-16 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200516_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Orplant', max_length=50),
        ),
    ]
