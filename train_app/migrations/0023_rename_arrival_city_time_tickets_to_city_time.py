# Generated by Django 4.0.4 on 2022-06-09 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('train_app', '0022_tickets_arrival_city_time_tickets_from_city_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='arrival_city_time',
            new_name='to_city_time',
        ),
    ]
