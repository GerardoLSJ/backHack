# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mxhacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='law',
            name='bullets',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='procedure',
            name='steps',
            field=models.TextField(default='', max_length=1000, null=True),
        ),
    ]
