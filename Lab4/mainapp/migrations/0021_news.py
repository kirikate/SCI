# Generated by Django 4.2.1 on 2023-09-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_alter_clientmodel_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('article', models.TextField(max_length=400)),
                ('author', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]