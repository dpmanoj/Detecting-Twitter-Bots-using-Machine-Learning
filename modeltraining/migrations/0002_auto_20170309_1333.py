# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeltraining', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users_app',
            old_name='profile_use_background_image_https',
            new_name='profile_use_background_image_url_https',
        ),
    ]
