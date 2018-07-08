# Generated by Django 2.0.6 on 2018-06-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheMainInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='主站标题')),
                ('main_url', models.URLField(max_length=150, verbose_name='跳转连接地址')),
            ],
            options={
                'verbose_name': '99站点跳转链接管理',
                'verbose_name_plural': '99站点跳转链接管理',
            },
        ),
    ]