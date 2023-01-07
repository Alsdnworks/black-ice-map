# Generated by Django 4.0.8 on 2023-01-06 08:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_moct_links_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='res_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_cost', models.CharField(max_length=255)),
                ('max_spd', models.IntegerField()),
                ('length', models.FloatField()),
                ('agg_cost', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('path_seq', models.IntegerField()),
                ('road_name', models.FloatField()),
            ],
        ),
    ]