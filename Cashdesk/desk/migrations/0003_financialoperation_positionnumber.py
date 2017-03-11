# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0002_auto_20170311_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialoperation',
            name='positionNumber',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
