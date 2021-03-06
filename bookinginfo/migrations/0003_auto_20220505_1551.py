# Generated by Django 3.2.12 on 2022-05-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinginfo', '0002_auto_20220505_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='busname',
            options={'ordering': ['bus_number', 'bus_name']},
        ),
        migrations.AlterField(
            model_name='busname',
            name='bus_number',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AddConstraint(
            model_name='busname',
            constraint=models.UniqueConstraint(fields=('bus_number', 'bus_name'), name='unique_busName'),
        ),
    ]
