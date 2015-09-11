# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roastlogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roastlogs',
            options={'managed': False, 'verbose_name_plural': 'Roast Logs'},
        ),
        migrations.AlterModelOptions(
            name='roasttimelogs',
            options={'managed': False, 'verbose_name_plural': 'Roast Time Logs'},
        ),
    ]
