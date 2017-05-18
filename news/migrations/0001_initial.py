# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
