# Generated by Django 4.0.8 on 2022-11-07 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_marker_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
