# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_at', models.DateField(null=True, blank=True)),
                ('output_at', models.DateField(null=True, blank=True)),
                ('status', models.IntegerField()),
                ('running_total', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_price', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('create_at', models.DateField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellingItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selling_price', models.IntegerField()),
            ],
            options={
                'db_table': 'selling_items',
                'managed': False,
            },
        ),
    ]
