# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandmanager', '0007_auto_20170108_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=0),
        ),
    ]
