# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0003_auto_20161202_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='gestalten.Gestalt'),
        ),
    ]
