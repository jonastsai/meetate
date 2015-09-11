# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': False, 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'managed': False, 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='sellingitems',
            options={'managed': False, 'verbose_name_plural': 'Selling Items'},
        ),
    ]
