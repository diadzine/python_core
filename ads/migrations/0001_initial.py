# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=510)),
                ('url', models.TextField(null=True)),
                ('secureUrl', models.TextField(null=True)),
                ('horizontal', models.PositiveSmallIntegerField(null=True)),
                ('vertical', models.PositiveSmallIntegerField(null=True)),
                ('square', models.PositiveSmallIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
