# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0007_vendors_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greencoffees',
            name='seller',
        ),
        migrations.AddField(
            model_name='greencoffees',
            name='vendor',
            field=models.ForeignKey(blank=True, to='greencoffees.Vendors', null=True),
        ),
    ]
