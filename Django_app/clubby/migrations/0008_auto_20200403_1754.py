# Generated by Django 3.0.4 on 2020-04-03 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubby', '0007_auto_20200403_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr_item',
            name='timed_out',
        ),
        migrations.AddField(
            model_name='qr_item',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 17, 54, 57, 727346)),
        ),
        migrations.AlterField(
            model_name='qr_item',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 17, 54, 57, 727346)),
        ),
        migrations.AlterField(
            model_name='rating',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 17, 54, 57, 720350)),
        ),
        migrations.AlterField(
            model_name='securityadvice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 3, 17, 54, 57, 726347)),
        ),
    ]