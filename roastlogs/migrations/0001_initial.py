# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0010_auto_20150911_0039'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roastlogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cust_index', models.CharField(max_length=20, null=True, blank=True)),
                ('comment', models.CharField(max_length=200, null=True, blank=True)),
                ('taste', models.CharField(max_length=200, null=True, blank=True)),
                ('score', models.IntegerField(null=True, blank=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('start_weight', models.IntegerField(null=True, blank=True)),
                ('end_weight', models.IntegerField(null=True, blank=True)),
                ('env_temp', models.IntegerField(null=True, blank=True)),
                ('env_humi', models.IntegerField(null=True, blank=True)),
                ('roastor_dev_id', models.CharField(max_length=10, null=True, blank=True)),
                ('order_of_day', models.IntegerField(null=True, blank=True)),
                ('category', models.IntegerField(null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('random_str', models.CharField(max_length=10, null=True, blank=True)),
                ('time_log_str', models.TextField(null=True, blank=True)),
                ('green_coffee', models.ForeignKey(blank=True, to='greencoffees.GreenCoffees', null=True)),
                ('roastor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'roastlogs',
                'verbose_name_plural': 'Roast Logs',
            },
        ),
        migrations.CreateModel(
            name='RoastTimelogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('second', models.IntegerField()),
                ('bt', models.IntegerField()),
                ('temp1', models.IntegerField(null=True, blank=True)),
                ('power', models.IntegerField(null=True, blank=True)),
                ('fan_level', models.IntegerField(null=True, blank=True)),
                ('roastlog', models.ForeignKey(blank=True, to='roastlogs.Roastlogs', null=True)),
            ],
            options={
                'db_table': 'roast_timelogs',
                'verbose_name_plural': 'Roast Time Logs',
            },
        ),
    ]
