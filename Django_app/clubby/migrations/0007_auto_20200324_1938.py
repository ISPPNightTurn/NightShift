# Generated by Django 3.0.4 on 2020-03-24 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0006_auto_20200324_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 19, 38, 25, 26344)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 24, 19, 38, 25, 25344)),
        ),
    ]
