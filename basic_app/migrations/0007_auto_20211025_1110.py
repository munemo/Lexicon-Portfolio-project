# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-10-25 09:10
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20211025_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkb0x',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Lord of the Ukasha', 'Lord of the Ukasha'), ('Venkatesans adventures in Stockholm', 'Venkatesans adventures in Stockholm'), ('Christoffer tales from KTH', 'Christoffer tales from KTH'), ('Marry the queen of Cebu', 'Marry the queen of Cebu')], max_length=200),
        ),
    ]