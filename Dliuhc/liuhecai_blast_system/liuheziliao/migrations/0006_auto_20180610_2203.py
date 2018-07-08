# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-10 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liuheziliao', '0005_auto_20180610_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indextopdata',
            name='_index_url',
        ),
        migrations.AddField(
            model_name='indextopdata',
            name='oneself_index_url',
            field=models.CharField(default=1, max_length=120, verbose_name='本站域名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indextopdata',
            name='name',
            field=models.CharField(max_length=120, verbose_name='首页上部广告位标题'),
        ),
        migrations.AlterField(
            model_name='indextopdata',
            name='standby_index_url',
            field=models.CharField(max_length=120, verbose_name='备用本站域名'),
        ),
    ]