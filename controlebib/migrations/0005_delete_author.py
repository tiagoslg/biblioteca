# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlebib', '0004_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]