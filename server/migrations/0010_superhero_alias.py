# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2021-02-09 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_auto_20210208_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='alias',
            field=models.CharField(default='', max_length=60),
        ),
    ]
