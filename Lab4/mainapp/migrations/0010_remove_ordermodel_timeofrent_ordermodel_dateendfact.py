# Generated by Django 4.2.1 on 2023-05-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_automodel_usagecount_carmodel_usagecount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='timeOfRent',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='dateEndFact',
            field=models.DateTimeField(null=True),
        ),
    ]
