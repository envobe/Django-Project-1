# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=20)),
                ('movie_catagory', models.CharField(max_length=30)),
                ('movie_director', models.CharField(max_length=20)),
                ('movie_producer', models.CharField(max_length=20)),
                ('movie_image', models.FileField(upload_to='')),
            ],
        ),
    ]
