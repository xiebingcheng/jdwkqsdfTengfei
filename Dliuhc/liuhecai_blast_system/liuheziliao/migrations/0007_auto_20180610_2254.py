# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-10 22:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liuheziliao', '0006_auto_20180610_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indextopdata',
            name='oneself_index_url',
        ),
        migrations.RemoveField(
            model_name='indextopdata',
            name='standby_index_url',
        ),
        migrations.RemoveField(
            model_name='oneselfdata',
            name='url',
        ),
    ]