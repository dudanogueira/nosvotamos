# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 11:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='dados',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='null'),
            preserve_default=False,
        ),
    ]
