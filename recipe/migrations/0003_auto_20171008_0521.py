# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20170923_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='created_at',
            new_name='create_at',
        ),
    ]
