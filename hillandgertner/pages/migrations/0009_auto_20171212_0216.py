# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20171212_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='protectedpage',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
