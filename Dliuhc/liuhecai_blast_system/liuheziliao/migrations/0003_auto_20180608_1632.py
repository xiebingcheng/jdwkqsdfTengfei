# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-08 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liuheziliao', '0002_auto_20180608_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Partner',
            new_name='AlliancePartner',
        ),
        migrations.RenameModel(
            old_name='mingzhan',
            new_name='FamousPartner',
        ),
        migrations.RenameModel(
            old_name='mianfei',
            new_name='FreeOpen',
        ),
        migrations.AlterModelOptions(
            name='alliancepartner',
            options={'verbose_name': '推荐同盟合作站', 'verbose_name_plural': '推荐同盟合作站'},
        ),
        migrations.AlterModelOptions(
            name='famouspartner',
            options={'verbose_name': '名站大流量合作', 'verbose_name_plural': '名站大流量合作'},
        ),
        migrations.AlterModelOptions(
            name='freeopen',
            options={'verbose_name': '免费公开资料', 'verbose_name_plural': '免费公开资料'},
        ),
        migrations.AlterModelOptions(
            name='oneselfdata',
            options={'verbose_name': '今晚免费精准资料', 'verbose_name_plural': '今晚免费精准资料'},
        ),
    ]