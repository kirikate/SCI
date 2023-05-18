# Generated by Django 4.2.1 on 2023-05-16 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('body', models.CharField(max_length=20)),
                ('price', models.BigIntegerField(default=56, null=True)),
                ('car_price', models.BigIntegerField(default=56, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f', models.CharField(max_length=30)),
                ('i', models.CharField(max_length=30)),
                ('o', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('adress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('percent', models.FloatField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PenaltyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('percent', models.FloatField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateBegin', models.DateTimeField()),
                ('dateEnd', models.DateTimeField()),
                ('timeOfRent', models.TimeField()),
                ('isActive', models.BooleanField()),
                ('price', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.automodel')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.clientmodel')),
                ('discounts', models.ManyToManyField(to='mainapp.discountmodel')),
                ('penalties', models.ManyToManyField(to='mainapp.penaltymodel')),
            ],
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='discounts',
            field=models.ManyToManyField(to='mainapp.discountmodel'),
        ),
        migrations.AddField(
            model_name='clientmodel',
            name='penalties',
            field=models.ManyToManyField(to='mainapp.penaltymodel'),
        ),
        migrations.AddField(
            model_name='automodel',
            name='carModel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.carmodel'),
        ),
    ]
