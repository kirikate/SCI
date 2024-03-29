# Generated by Django 4.2.1 on 2023-05-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_rename_car_ordermodel_auto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='dateEndFact',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='discounts',
            field=models.ManyToManyField(default=None, to='mainapp.discountmodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='penalties',
            field=models.ManyToManyField(default=None, to='mainapp.penaltymodel'),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
