# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-05 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatars/default.png', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='desc',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
