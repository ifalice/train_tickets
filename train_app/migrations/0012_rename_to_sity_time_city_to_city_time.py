# Generated by Django 4.0.4 on 2022-05-07 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_app', '0011_alter_city_from_city_time_alter_city_to_sity_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='to_sity_time',
            new_name='to_city_time',
        ),
    ]
