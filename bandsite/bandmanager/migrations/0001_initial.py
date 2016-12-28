# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 06:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(blank=True, max_length=200)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandmanager.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandmanager.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('difficulty', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandmanager.Band')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bandmanager.Member')),
            ],
        ),
    ]