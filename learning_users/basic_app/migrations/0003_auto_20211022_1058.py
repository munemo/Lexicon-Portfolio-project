# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-22 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_subscriberinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriberinfo',
            name='subscriber',
        ),
        migrations.AlterField(
            model_name='subscriberinfo',
            name='subscriber_email',
            field=models.EmailField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
