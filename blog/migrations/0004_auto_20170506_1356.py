# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170506_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='修改时间'),
        ),
    ]