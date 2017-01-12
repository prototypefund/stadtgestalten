# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0010_auto_20160923_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships_created', to='gestalten.Gestalt'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='gestalten.Gestalt'),
        ),
    ]
