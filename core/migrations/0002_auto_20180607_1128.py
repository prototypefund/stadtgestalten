# Generated by Django 2.0.5 on 2018-06-07 09:28

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissiontoken',
            name='secret_key',
            field=models.CharField(default=core.models.generate_token, max_length=15, unique=True),
        ),
    ]
