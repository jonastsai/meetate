# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0005_greencoffees_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('tel', models.CharField(max_length=30, null=True, blank=True)),
                ('mobile', models.CharField(max_length=30, null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('web_page', models.CharField(max_length=100, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'Vendors',
                'verbose_name_plural': 'Green Coffee Vendor',
            },
        ),
    ]
