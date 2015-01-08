# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloggers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=510)),
                ('biography', models.TextField(null=True)),
                ('linkResults', models.TextField(null=True)),
                ('profilePic', models.TextField(null=True)),
                ('sponsors', models.TextField(null=True)),
                ('ad', models.TextField(null=True)),
                ('header', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(null=True)),
                ('blogId', models.SmallIntegerField(null=True, db_index=True)),
                ('date', models.DateTimeField(db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
