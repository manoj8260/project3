# Generated by Django 5.0.7 on 2024-10-22 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('company', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='bike_photos')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renter.brand')),
            ],
        ),
    ]
