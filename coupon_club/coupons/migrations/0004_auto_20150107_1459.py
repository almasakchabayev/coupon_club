# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_auto_20150107_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='image_url',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='conditions',
            field=models.TextField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='deal_url',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='discount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='new_price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='old_price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='title',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deal',
            name='website',
            field=models.ForeignKey(related_name='deals', blank=True, to='coupons.Website'),
            preserve_default=True,
        ),
    ]
