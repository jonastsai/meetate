# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='greencoffees',
            options={'managed': False, 'verbose_name_plural': 'Green Coffees'},
        ),
    ]
