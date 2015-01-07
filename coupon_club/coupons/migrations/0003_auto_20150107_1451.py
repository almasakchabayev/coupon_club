# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20150101_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='company',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='description',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='discount_percentage',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='discount_text',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='end_date_time',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='price',
        ),
        migrations.AddField(
            model_name='deal',
            name='conditions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='discount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='new_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='old_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deal',
            name='deal_url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
