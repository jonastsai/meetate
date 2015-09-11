# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0006_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='contact',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
