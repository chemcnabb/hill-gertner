# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171121_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body_text_color',
            field=models.CharField(default='#000', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='body_text_size',
            field=models.IntegerField(default=12, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='heading_text_color',
            field=models.CharField(default='#000', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='heading_text_size',
            field=models.IntegerField(default=10, null=True),
        ),
    ]
