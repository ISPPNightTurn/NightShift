# Generated by Django 3.0.4 on 2020-03-29 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0010_auto_20200329_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 15, 48, 20, 677189)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 15, 48, 20, 676192)),
        ),
    ]
