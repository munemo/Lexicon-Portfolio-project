# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-21 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='description',
            field=models.CharField(default='description', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='skills',
            field=models.CharField(default='skills', max_length=200),
        ),
    ]
