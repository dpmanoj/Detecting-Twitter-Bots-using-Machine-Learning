# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeltraining', '0015_auto_20170309_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers_app',
            name='bot',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='friends_app',
            name='bot',
            field=models.BooleanField(default=False),
        ),
    ]