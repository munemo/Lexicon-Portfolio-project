# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-27 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20211027_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='media/profile_pics/harry.jpeg', upload_to='profile_pics'),
        ),
    ]
