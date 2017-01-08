# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bandmanager', '0003_taskcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcomment',
            name='commenter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='bandmanager.Member'),
            preserve_default=False,
        ),
    ]
