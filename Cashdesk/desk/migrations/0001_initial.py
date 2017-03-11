# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialOperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430')),
                ('amount', models.FloatField(verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('isSpent', models.BooleanField(verbose_name='\u0420\u0430\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044f')),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
    ]
