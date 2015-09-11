# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0009_auto_20150911_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greencoffees',
            name='vendor',
            field=models.ForeignKey(to='greencoffees.Vendors'),
        ),
    ]
