# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info', models.TextField(max_length=255)),
                ('category', models.CharField(max_length=255, db_index=True)),
                ('genre', models.TextField(max_length=255)),
                ('link', models.TextField(max_length=511)),
                ('location', models.TextField(max_length=255)),
                ('discipline', models.TextField(max_length=255)),
                ('raceId', models.IntegerField(db_index=True)),
                ('table', models.TextField()),
                ('date', models.IntegerField(db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
