# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeltraining', '0006_auto_20170309_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets_app',
            name='retweeted_status_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
