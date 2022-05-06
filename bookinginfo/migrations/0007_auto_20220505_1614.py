# Generated by Django 3.2.12 on 2022-05-05 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinginfo', '0006_auto_20220505_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'ordering': ['service', 'user']},
        ),
        migrations.AlterModelOptions(
            name='locationdetail',
            options={'ordering': ['location_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['bus', 'trip_direction', 'semester']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AddConstraint(
            model_name='enrollment',
            constraint=models.UniqueConstraint(fields=('service', 'user'), name='unique_enrollment'),
        ),
        migrations.AddConstraint(
            model_name='locationdetail',
            constraint=models.UniqueConstraint(fields=('location_name', 'disambiguator'), name='unique_location'),
        ),
        migrations.AddConstraint(
            model_name='service',
            constraint=models.UniqueConstraint(fields=('semester', 'bus', 'trip_direction'), name='unique_service'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_user'),
        ),
    ]