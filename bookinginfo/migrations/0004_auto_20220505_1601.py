# Generated by Django 3.2.12 on 2022-05-05 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinginfo', '0003_auto_20220505_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ['period_sequence']},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['year__year', 'period__period_sequence']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['year']},
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddConstraint(
            model_name='semester',
            constraint=models.UniqueConstraint(fields=('year', 'period'), name='unique_semester'),
        ),
    ]