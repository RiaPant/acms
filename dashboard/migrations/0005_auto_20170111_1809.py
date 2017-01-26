# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20170108_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('locker_id', models.IntegerField(primary_key=True, serialize=False)),
                ('locker_name', models.CharField(blank=True, db_column='Locker_name', max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('state', models.CharField(blank=True, max_length=45, null=True)),
                ('pincode', models.CharField(blank=True, max_length=45, null=True)),
                ('locker_capacity', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'table1',
            },
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('empty_slots', models.CharField(blank=True, max_length=45, null=True)),
                ('filler_slots', models.CharField(blank=True, max_length=45, null=True)),
                ('no_of_lockers', models.CharField(blank=True, max_length=45, null=True)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'table2',
            },
        ),
        migrations.DeleteModel(
            name='TblName',
        ),
    ]