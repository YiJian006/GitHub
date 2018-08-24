# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20180803_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='用户')),
                ('ads', models.CharField(max_length=200, verbose_name='地址')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '地址信息',
                'verbose_name_plural': '地址信息',
                'db_table': 'Address',
            },
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='isban',
            field=models.BooleanField(default=False, verbose_name='禁用'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='isdelete',
            field=models.BooleanField(default=False, verbose_name='删除'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=200, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='注册时间'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userinfo.UserInfo'),
        ),
    ]
