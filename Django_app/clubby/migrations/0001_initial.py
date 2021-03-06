# Generated by Django 3.0.4 on 2020-04-03 10:29

import clubby.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of your club.', max_length=50)),
                ('address', models.CharField(help_text='Enter the full address so google maps can find it.', max_length=200)),
                ('max_capacity', models.PositiveIntegerField(help_text="The capacity of your club, you're responsible for the enforcement of this number.")),
                ('NIF', models.CharField(help_text='Company number for the club', max_length=10)),
                ('picture', models.URLField(blank=True, help_text='URL to a picture of your club', null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('picture', models.URLField(blank=True, help_text='URL to the poster for the event', null=True)),
                ('start_time', models.PositiveIntegerField(blank=True, choices=[(0, 0), (23, 23), (22, 22), (21, 21), (20, 20), (19, 19), (18, 18), (17, 17), (16, 16), (15, 15), (14, 14), (13, 13), (12, 12), (11, 11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=0, help_text='event start time 24h format.')),
                ('duration', models.PositiveIntegerField(blank=True, choices=[(12, 12), (11, 11), (10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=0, help_text='event duration in hours, max is 12 hours.')),
                ('event_type', models.CharField(blank=True, choices=[('rock', 'rock'), ('pop', 'pop'), ('techno', 'techno'), ('hip hop', 'hip hop'), ('trap', 'trap'), ('reggaeton', 'reggaeton'), ('indie', 'indie'), ('metal', 'metal'), ('latino', 'latino')], default='reggaeton', help_text='event music type', max_length=100)),
                ('atendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_type', models.CharField(blank=True, choices=[('r', 'refreshment'), ('c', 'cocktail'), ('s', 'shot'), ('b', 'beer'), ('w', 'wine'), ('k', 'snack'), ('h', 'hookah'), ('m', 'misc.')], default='m', help_text='product type', max_length=1)),
                ('reservation_exclusive', models.BooleanField()),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Club')),
            ],
            options={
                'ordering': ('reservation_exclusive', 'product_type'),
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.CharField(default='Basic', help_text='The name of the type of ticket you are trying to sell.', max_length=40)),
                ('description', models.TextField(default='this allows you to enter the party.', help_text='Decribe what this ticket entices.')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('category', 'price'),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('stars', models.IntegerField(help_text='star rating 1-10')),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 4, 3, 12, 29, 15, 997830))),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Club')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QR_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_used', models.BooleanField(default=False)),
                ('priv_key', models.CharField(max_length=128)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2020, 4, 3, 12, 29, 15, 997830))),
                ('timed_out', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubby.Product')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubby.Ticket')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('funds', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('picture', models.URLField(blank=True, help_text='Post a picture of your pretty face, dude', null=True)),
                ('renew_premium', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('is_user', 'Is a user and can do everything an identified user can.'), ('is_owner', 'Is an owner and can do everything an identified owner can.'), ('is_premium_owner', 'Is a premium owner and can do everything an identified owner can and more.')),
            },
        ),
        migrations.CreateModel(
            name='CreateTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('category', models.CharField(default='Basic', help_text='The name of the type of ticket you are trying to sell.', max_length=40)),
                ('description', models.TextField(default='this allows you to enter the party.', help_text='Decribe what this ticket entices.', max_length=40)),
                ('size', clubby.models.IntegerRangeField(default=1, help_text='Number of tickets. (Max)')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubby.Event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
