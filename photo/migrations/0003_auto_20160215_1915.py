# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-15 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20160215_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='filtered_image_file',
            field=models.ImageField(upload_to='static_files/uploaded/filtered/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image_file',
            field=models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d'),
        ),
    ]
