# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20161127_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='img',
        ),
    ]