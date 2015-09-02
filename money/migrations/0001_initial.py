# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('sortcode', models.CharField(max_length=8)),
                ('account', models.CharField(max_length=8)),
                ('accounttype', models.CharField(max_length=20)),
                ('currentcy', models.CharField(max_length=1)),
            ],
        ),
    ]
