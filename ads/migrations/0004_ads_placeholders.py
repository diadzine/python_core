# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20151029_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='placeholders',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, max_length=165, null=True, choices=[(b'actu-top', b'Page Actu, haut de page'), (b'actu-side', b'Page Actu, colonne droite'), (b'actu-bottom', b'Page Actu, base de page'), (b'results-top', b'Pages R\xc3\xa9sultats, haut de page'), (b'results-side', b'Pages R\xc3\xa9sultats, colonne droite'), (b'results-bottom', b'Pages R\xc3\xa9sultats, base de page'), (b'blog-top', b'Pages Blog, haut de page'), (b'blog-side', b'Pages Blog, colonne droite'), (b'blog-bottom', b'Pages Blog, base de page'), (b'shop-top', b'Page Angulation, haut de page'), (b'shop-bottom', b'Page Angulation, base de page'), (b'sponsors-top', b'Page Mentors & Sponsors, haut de page'), (b'sponsors-side', b'Page Mentors & Sponsors, colonne droite'), (b'sponsors-bottom', b'Page Mentors & Sponsors, base de page')]),
            preserve_default=True,
        ),
    ]
