# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-18 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20170614_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]