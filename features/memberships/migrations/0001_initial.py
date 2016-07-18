# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0038_auto_20160718_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('gestalt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Gestalt')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.Group')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('gestalt', 'group')]),
        ),
    ]