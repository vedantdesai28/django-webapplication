# Generated by Django 3.2.12 on 2022-05-05 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookinginfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='busname',
            old_name='bus_direction',
            new_name='bus_name',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='trip_name',
            new_name='trip_direction',
        ),
    ]
