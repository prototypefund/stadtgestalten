# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 07:56
from __future__ import unicode_literals

from django.db import migrations
import grouprise.features.stadt.models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0017_auto_20171127_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=grouprise.features.stadt.models.EntitySlugField(blank=True, help_text='Wird auch als Kurzname verwendet', null=True, unique=True, verbose_name='Adresse der Gruppenseite'),
        ),
    ]
