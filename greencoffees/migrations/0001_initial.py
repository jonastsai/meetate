# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenCoffees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30, null=True, blank=True)),
                ('manor', models.CharField(max_length=30, null=True, blank=True)),
                ('process', models.IntegerField()),
                ('price', models.IntegerField()),
                ('qty_in', models.IntegerField()),
                ('qty_now', models.IntegerField(null=True, blank=True)),
                ('defect', models.IntegerField(null=True, blank=True)),
                ('seller', models.CharField(max_length=30, null=True, blank=True)),
                ('official_taste', models.CharField(max_length=100, null=True, blank=True)),
                ('official_desc', models.TextField(null=True, blank=True)),
                ('self_taste', models.CharField(max_length=60, null=True, blank=True)),
                ('create_at', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'green_coffees',
                'managed': False,
            },
        ),
    ]
