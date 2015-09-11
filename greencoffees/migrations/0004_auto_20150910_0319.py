# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greencoffees', '0003_auto_20150910_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='greencoffees',
            name='grade',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='greencoffees',
            name='process',
            field=models.IntegerField(choices=[(0, '\u6c34\u6d17'), (1, '\u65e5\u66ec'), (2, '\u871c\u8655\u7406')]),
        ),
    ]
