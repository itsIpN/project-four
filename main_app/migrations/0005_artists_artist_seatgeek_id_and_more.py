# Generated by Django 4.1.2 on 2022-10-08 18:08

from django.db import migrations, models
import enum


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_artists_user_remove_followedevent_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artists',
            name='artist_seatgeek_id',
            field=models.IntegerField(default=0, verbose_name=enum.unique),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artists',
            name='artist_spotify_uri',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
