# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150819_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 17, 36, 30, 651685, tzinfo=utc), verbose_name='date added'),
            preserve_default=False,
        ),
    ]
