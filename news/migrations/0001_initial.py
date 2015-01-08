# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('mag', models.SmallIntegerField(null=True, db_index=True)),
                ('date', models.DateTimeField(db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OldNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titre', models.TextField(null=True)),
                ('Date', models.TextField(null=True)),
                ('Texte', models.TextField(null=True)),
                ('Auteur', models.TextField(null=True)),
                ('Analyse', models.BooleanField(default=False)),
                ('Resultats', models.BooleanField(default=False)),
                ('Interview', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
