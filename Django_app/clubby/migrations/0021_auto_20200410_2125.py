# Generated by Django 3.0.3 on 2020-04-10 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0020_auto_20200410_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='spotify_refresh_token',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name='qr_item',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 21, 25, 13, 693733)),
        ),
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 21, 25, 13, 693733)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 21, 25, 13, 692733)),
        ),
        migrations.AlterField(
            model_name='securityadvice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 21, 25, 13, 693733)),
        ),
    ]
