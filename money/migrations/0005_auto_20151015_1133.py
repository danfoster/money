# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0004_auto_20150907_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='transaction',
            name='memo',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='payee',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transid',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transtype',
            field=models.CharField(default=b'pos', max_length=10),
        ),
    ]
