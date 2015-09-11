# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0002_auto_20150910_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='greencoffees',
            options={'verbose_name_plural': 'Green Coffees'},
        ),
    ]
