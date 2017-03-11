# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0003_financialoperation_positionnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialoperation',
            name='whoPayed',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
