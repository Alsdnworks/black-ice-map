# Generated by Django 4.0.8 on 2022-11-05 16:18

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_link_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='location',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
