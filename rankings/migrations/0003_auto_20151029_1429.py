# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0002_auto_20150109_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='races',
            name='table',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
