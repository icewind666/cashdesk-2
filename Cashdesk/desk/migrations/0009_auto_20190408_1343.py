# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-08 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk', '0008_auto_20190406_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialoperation',
            name='positionNumberPromSold',
            field=models.TextField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='financialoperation',
            name='positionNumber',
            field=models.BigIntegerField(),
        ),
    ]
