# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protected_pages', '0007_auto_20180107_2103'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='image',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]