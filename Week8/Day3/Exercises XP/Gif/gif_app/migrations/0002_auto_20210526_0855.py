# Generated by Django 3.1.7 on 2021-05-26 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gif_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(blank=True, related_name='all_gifs', to='gif_app.Gif'),
        ),
    ]