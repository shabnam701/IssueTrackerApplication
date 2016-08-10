# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-09 18:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdOn',
            field=models.DateField(default=datetime.date(2016, 8, 9)),
        ),
        migrations.AlterField(
            model_name='post',
            name='dueDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('NEW', 'new'), ('INPROGRESS', 'inprogress'), ('RESOLVED', 'resolved'), ('FEEDBACK', 'feedback'), ('CLOSED', 'closed')], max_length=20),
        ),
    ]