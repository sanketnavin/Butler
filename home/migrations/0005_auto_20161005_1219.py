# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_otp_otp_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='otp_verified',
            field=models.NullBooleanField(default=False),
        ),
    ]