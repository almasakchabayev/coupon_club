# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0005_auto_20150107_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='deal',
            name='website',
            field=models.ForeignKey(related_name='deals', to='coupons.Website'),
            preserve_default=True,
        ),
    ]
