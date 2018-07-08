# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-21 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liuheziliao', '0008_oneselfdata_wechat_img_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeChatQRCodeImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='微信二维码说明')),
                ('wechat_img_qr_code', models.ImageField(upload_to='img', verbose_name='微信二维码图片上传地址')),
            ],
            options={
                'verbose_name': '微信二维码图片上传',
                'verbose_name_plural': '微信二维码图片上传',
            },
        ),
        migrations.RemoveField(
            model_name='oneselfdata',
            name='wechat_img_qr_code',
        ),
    ]