# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 22:23
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='img',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='img/logo'),
        ),
    ]
