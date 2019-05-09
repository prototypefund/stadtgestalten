# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 15:29
from __future__ import unicode_literals

import grouprise.core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0013_auto_20170622_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='avatar',
            field=grouprise.core.models.ImageField(blank=True, help_text='Mögliche Formate sind JPEG, PNG und viele weitere. Nicht unterstützt werden PDF- oder SVG-Dateien. Die maximal erlaubte Dateigröße beträgt 5 MB.', upload_to=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='logo',
            field=grouprise.core.models.ImageField(blank=True, help_text='Mögliche Formate sind JPEG, PNG und viele weitere. Nicht unterstützt werden PDF- oder SVG-Dateien. Die maximal erlaubte Dateigröße beträgt 5 MB.', upload_to=''),
        ),
    ]
