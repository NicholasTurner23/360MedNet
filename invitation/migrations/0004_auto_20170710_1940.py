# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-10 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0003_auto_20170708_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]