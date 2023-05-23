# Generated by Django 4.2.1 on 2023-05-16 13:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_carmodel_car_price_alter_carmodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(2010)]),
        ),
    ]