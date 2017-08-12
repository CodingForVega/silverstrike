# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyaccountant', '0013_auto_20170811_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='show_on_dashboard',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='internal_type',
            field=models.IntegerField(choices=[(1, 'Personal'), (2, 'Revenue'), (3, 'Expense'), (4, 'System')], default=1),
        ),
    ]