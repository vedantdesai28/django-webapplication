# Generated by Django 3.2.12 on 2022-05-05 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookinginfo', '0005_alter_busname_bus_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enrollment',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user_id',
            new_name='user',
        ),
    ]
