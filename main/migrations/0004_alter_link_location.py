# Generated by Django 4.1 on 2022-11-04 05:38

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_link_id_link_link_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='location',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]