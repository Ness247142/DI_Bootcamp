# Generated by Django 3.1.7 on 2021-03-11 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('released_date', models.DateField(default=datetime.datetime(2021, 3, 11, 16, 10, 18, 522161))),
            ],
        ),
    ]