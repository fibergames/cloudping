# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-20 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0006_auto_20180113_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='description',
        ),
        migrations.AddField(
            model_name='company',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
