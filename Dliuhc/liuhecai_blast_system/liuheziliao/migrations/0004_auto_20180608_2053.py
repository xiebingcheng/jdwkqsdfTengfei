# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-08 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liuheziliao', '0003_auto_20180608_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrityNetworkTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='诚信网投专区')),
                ('url', models.URLField(max_length=300, verbose_name='网投专区链接跳转地址')),
            ],
            options={
                'verbose_name': '诚信网投专区',
                'verbose_name_plural': '诚信网投专区',
            },
        ),
        migrations.AddField(
            model_name='oneselfdata',
            name='content',
            field=models.TextField(default='', verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='famouspartner',
            name='url',
            field=models.URLField(max_length=300, verbose_name='名站大流量合作站跳转地址'),
        ),
        migrations.AlterField(
            model_name='freeopen',
            name='url',
            field=models.URLField(max_length=300, verbose_name='免费公开资料跳转地址'),
        ),
        migrations.AlterField(
            model_name='oneselfdata',
            name='url',
            field=models.URLField(max_length=300, verbose_name='今晚免费精准资料跳转地址'),
        ),
    ]
