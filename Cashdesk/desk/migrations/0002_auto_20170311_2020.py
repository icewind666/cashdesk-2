# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialoperation',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='financialoperation',
            name='isSpent',
        ),
        migrations.AddField(
            model_name='financialoperation',
            name='fileLink',
            field=models.TextField(default='-', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='financialoperation',
            name='isClosed',
            field=models.BooleanField(default=0, verbose_name='\u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u043e\u043f\u043b\u0430\u0447\u0435\u043d\u043e'),
            preserve_default=False,
        ),
    ]
