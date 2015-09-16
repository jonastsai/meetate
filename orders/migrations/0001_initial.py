# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0010_auto_20150911_0039'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roastlogs', '0002_remove_roastlogs_green_coffee'),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
                'verbose_name_plural': 'Orders',
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
                ('green_coffee', models.ForeignKey(to='greencoffees.GreenCoffees')),
            ],
            options={
                'db_table': 'products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='SellingItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selling_price', models.IntegerField()),
                ('order', models.ForeignKey(to='orders.Orders')),
                ('product', models.ForeignKey(to='orders.Products')),
                ('roastlog', models.ForeignKey(blank=True, to='roastlogs.Roastlogs', null=True)),
            ],
            options={
                'db_table': 'selling_items',
                'verbose_name_plural': 'Selling Items',
            },
        ),
    ]
