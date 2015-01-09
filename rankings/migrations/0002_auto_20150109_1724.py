# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='races',
            name='category',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='date',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='discipline',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='genre',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='info',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='link',
            field=models.TextField(max_length=511, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='location',
            field=models.TextField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='races',
            name='raceId',
            field=models.IntegerField(db_index=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
