# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_auto_20150107_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='tag',
        ),
        migrations.AlterField(
            model_name='deal',
            name='website',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]
