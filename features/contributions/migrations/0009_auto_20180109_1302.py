# Generated by Django 2.0.1 on 2018-01-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0008_contribution_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contribution',
            name='attached_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attachments', to='contributions.Contribution'),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contributions', to='gestalten.Gestalt'),
        ),
        migrations.AlterField(
            model_name='contribution',
            name='in_reply_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='contributions.Contribution'),
        ),
    ]
