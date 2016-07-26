# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0041_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='closed',
            field=models.BooleanField(default=False, help_text='Nur Mitglieder können neue Mitglieder aufnehmen.', verbose_name='Geschlossene Gruppe'),
        ),
    ]
