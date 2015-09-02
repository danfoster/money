# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_auto_20150901_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='currentcy',
        ),
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(default=b'\xc2\xa3', max_length=1),
        ),
    ]
