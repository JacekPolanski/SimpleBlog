# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150820_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
