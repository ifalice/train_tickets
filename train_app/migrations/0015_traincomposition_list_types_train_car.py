# Generated by Django 4.0.4 on 2022-05-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train_app', '0014_traincomposition_typetraincars_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='traincomposition',
            name='list_types_train_car',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
