# Generated by Django 5.1.4 on 2024-12-22 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0002_savedpointsearch"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="osmpoint",
            table="planet_osm_point",
        ),
    ]
