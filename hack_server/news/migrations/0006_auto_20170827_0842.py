# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170827_0254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporter',
            old_name='rate',
            new_name='start',
        ),
        migrations.AddField(
            model_name='reporter',
            name='bad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reporter',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]
