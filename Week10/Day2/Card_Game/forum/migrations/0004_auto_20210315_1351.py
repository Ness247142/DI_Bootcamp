# Generated by Django 3.1.7 on 2021-03-15 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_profile_species'),
        ('forum', '0003_auto_20210315_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='thread_id',
            new_name='index',
        ),
        migrations.AlterField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.profile'),
        ),
        migrations.AlterField(
            model_name='index',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.profile'),
        ),
    ]
