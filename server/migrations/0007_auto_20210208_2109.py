# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2021-02-09 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20210208_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
    ]
