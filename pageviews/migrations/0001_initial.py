# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HitCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('url', models.CharField(max_length=2000, verbose_name='URL')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='Hits')),
            ],
            options={
                'ordering': ('-created', '-modified'),
                'get_latest_by': 'created',
            },
            bases=(models.Model,),
        ),
    ]
