# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0006_auto_20150108_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='website',
            field=models.ForeignKey(related_name='deals', blank=True, to='coupons.Website'),
            preserve_default=True,
        ),
    ]
