# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from coupons import models

import django
django.setup()

class CouponScraperPipeline(object):
    def process_item(self, item, spider):
        deal, deal_created = models.Deal.objects.get_or_create(
            deal_url=item['deal_url'],
        )
        chocolife, created = models.Website.objects.get_or_create(
            name='chocolife',
            url='http://www.chocolife.kz'
        )
        if deal_created:
            deal.title = item['title']
            deal.old_price = item['old_price']
            deal.new_price = item['new_price']
            deal.number_of_purchases = item['number_of_purchases']
            deal.discount = item['discount']
            deal.conditions = item['conditions']
            deal.image_url = item['image_url']
            # deal.tag = item['tag']
            if 'choco' in item['website']:
                deal.website = chocolife
        else:
            deal.number_of_purchases = item['number_of_purchases']

        deal.save()
        return item