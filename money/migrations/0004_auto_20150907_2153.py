# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0003_auto_20150901_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='accounttype',
            field=models.CharField(default=b'CUR', max_length=3, verbose_name=b'Account Type', choices=[(b'CUR', b'Current'), (b'SAV', b'Savings'), (b'CR', b'Credit Card')]),
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.CharField(default=b'S', max_length=1, choices=[(b'S', b'\xc2\xa3')]),
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(to='money.Account'),
        ),
    ]
