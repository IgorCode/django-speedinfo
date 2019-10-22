# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-18 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=255, verbose_name=b'View name')),
                ('method', models.CharField(max_length=8, verbose_name=b'HTTP method')),
                ('anon_calls', models.PositiveIntegerField(default=0, verbose_name=b'Anonymous calls')),
                ('cache_hits', models.PositiveIntegerField(default=0, verbose_name=b'Cache hits')),
                ('sql_total_time', models.FloatField(default=0, verbose_name=b'SQL total time')),
                ('sql_total_count', models.PositiveIntegerField(default=0, verbose_name=b'SQL total queries count')),
                ('total_calls', models.PositiveIntegerField(default=0, verbose_name=b'Total calls')),
                ('total_time', models.FloatField(default=0, verbose_name=b'Total time')),
            ],
            options={
                'db_table': 'speedinfo_storage_database',
            },
        ),
        migrations.AlterUniqueTogether(
            name='storage',
            unique_together=set([('view_name', 'method')]),
        ),
    ]