# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0004_financialoperation_whopayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialoperation',
            name='alreadyPayed',
            field=models.FloatField(default=0, verbose_name='\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e'),
            preserve_default=False,
        ),
    ]
