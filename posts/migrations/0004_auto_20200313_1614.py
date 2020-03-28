# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200313_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('r', 'Рассказ'), ('p', 'Поэма'), ('rr', 'Рассказ')], default='r', max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(default='...'),
        ),
    ]
