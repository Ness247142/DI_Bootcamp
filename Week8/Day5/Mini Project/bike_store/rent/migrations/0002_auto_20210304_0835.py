# Generated by Django 3.1.7 on 2021-03-04 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalrate',
            name='daily_rate',
            field=models.FloatField(),
        ),
    ]
