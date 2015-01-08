# -*- coding: utf-8 -*-
import re

from datetime import datetime
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from coupon_scraper.items import DealItem
from coupon_scraper.spiders.utils import clean_extract, get_numbers_from_string


class MySpider(Spider):
    name = 'chocolife'
    allowed_domains = [
        'chocolife.me'
    ]
    start_urls = [
        'http://www.chocolife.me',
    ]

    def parse(self, response):
        sel = Selector(response)
        deals = sel.xpath('//li[@class="b-deal"]')

        for deal in deals:
            item = DealItem()
            item['website'] = 'chocolife'
            item['website_url'] = 'http://www.chocolife.me/'
            # need to finish
            # categories = clean_extract(
            #     deal,
            #     './/@data-categories',
            # )
            raw_discount = clean_extract(
                deal, 
                'span.e-deal__discount ::text',
            )
            item['discount'] = get_numbers_from_string(raw_discount)
            item['title'] = clean_extract(
                deal, 
                'h2.e-deal__title ::text',
            )
            item['summary_front'] = clean_extract(
                deal, 
                'p.e-deal__text ::text',
            )
            raw_number_of_purchases = clean_extract(
                deal, 
                'span.e-deal__link ::text',
            )
            item['number_of_purchases'] = get_numbers_from_string(raw_number_of_purchases)
            item['image_url'] = 'http://www.chocolife.me' + clean_extract(
                deal,
                'img.e-deal__img ::attr(data-original)',
            )
            raw_old_price = clean_extract(
                deal,
                'span.e-deal__price--old ::text',
                0
            )
            item['old_price'] = get_numbers_from_string(raw_old_price)
            raw_new_price = clean_extract(
                deal,
                'span.e-deal__price ::text',
                -1
            )
            item['new_price'] = get_numbers_from_string(raw_new_price)
            item['deal_url'] = clean_extract(
                deal,
                'a.e-link--deal ::attr(href)',
            )
            request = Request(
                item['deal_url'],
                callback=self.parse_deal_info
            )
            request.meta['item'] = item
            yield request


    def parse_deal_info(self, response):
        item = response.meta['item']
        sel = Selector(response)
        # item['address'] = clean_extract(
        #     sel,
        #     '//li[@class="e-offer__feature "]/text()', 
        # )
        # item['info'] = clean_extract(
        #     sel,
        #     './/p[@class="e-offer__description"]/text()',
        # )
        item['conditions'] = clean_extract(
            sel,
            'ul.b-conditions-list',
        )
        # raw_end_timestamp = clean_extract(
        #     sel,
        #     'p.js-e-offer__expire-date ::text',
        #     'css'
        # )
        # if raw_end_timestamp != '':
        #     item['end_timestamp'] = int(raw_end_timestamp) / 1000
        # else:
        #     item['end_timestamp'] = 0

        # address_path = sel.css(':contains("%s")' % u'г. Алматы')
        # if '<b>' in address_path.extract() and len(address_path.extract())<200:
        #     item['address'] = address_path.extract()
        # else:
        #     item['address'] = 'ok'


            # some = address_path.xpath('.//text()[name(..)="b"').extract()
        # offer_features = sel.css('ul.b-offer__features-list li')
        # if len(offer_features) > 1:
        #     item['address'] = offer_features[0].xpath('b/text').extract()
        yield item
        # print item['address']
        # print item['end_timestamp']