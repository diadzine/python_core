# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ads_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='link',
            field=models.TextField(default=b'', null=True),
            preserve_default=True,
        ),
    ]
