# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_auto_20161125_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='all_day',
            field=models.BooleanField(default=False, verbose_name='ganztägig'),
        ),
        migrations.AddField(
            model_name='event',
            name='until_time',
            field=models.DateTimeField(null=True, verbose_name='Datum / Uhrzeit Ende'),
        ),
    ]