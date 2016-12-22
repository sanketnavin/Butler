# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-02 17:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkFurniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('latitude', models.FloatField(default=1.0, null=True)),
                ('longitude', models.FloatField(default=1.0, null=True)),
                ('place_id', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=1000)),
                ('contact', models.CharField(default='1', max_length=100, null=True)),
                ('open_now', models.CharField(default='1000', max_length=1000, null=True)),
                ('open_time', models.CharField(default='1000', max_length=1000, null=True)),
                ('close_time', models.CharField(default='1000', max_length=1000, null=True)),
                ('rating', models.CharField(default='Null', max_length=1000, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('place_id', models.CharField(max_length=1000)),
                ('img', models.CharField(max_length=1000)),
                ('contact', models.CharField(max_length=100, null=True)),
                ('open_now', models.CharField(max_length=1000, null=True)),
                ('open_time', models.CharField(max_length=1000, null=True)),
                ('close_time', models.CharField(max_length=1000, null=True)),
                ('rating', models.CharField(default='Null', max_length=1000, null=True)),
                ('is_bookmarked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeservices_thumb', models.CharField(max_length=1000)),
            ],
        ),
    ]