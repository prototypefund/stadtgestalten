# Generated by Django 2.0.1 on 2018-01-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170921_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='votes', to='gestalten.Gestalt'),
        ),
    ]
