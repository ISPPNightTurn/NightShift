# Generated by Django 3.0.4 on 2020-03-28 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 17, 7, 18, 84701)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 28, 17, 7, 18, 84701)),
        ),
    ]
