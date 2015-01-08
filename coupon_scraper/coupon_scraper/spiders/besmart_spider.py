from datetime import datetime
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from coupon_scraper.items import DealItem

from coupon_scraper.spiders.utils import clean_extract, get_numbers_from_string, drop_html_tags

# def clean_extract(some_selector,xpath_of_info):
#     try:
#         clean_value_list = some_selector.xpath(xpath_of_info).extract()
#         i=0
#         clean_value=''
#         for i in range(0, len(clean_value_list)):
            
#             clean_value=clean_value+clean_value_list[i]
#             i+=1
#     except:
#         clean_value = ''
#     return clean_value


class BesmartSpider(Spider):
    name = 'besmart'
    allowed_domains = [
        'besmart.kz'
    ]
    start_urls = [
        'http://besmart.kz',
    ]

    def parse(self, response):
        sel = Selector(response)
        deals = sel.xpath('//li[@class="span6"]')
        for deal in deals:
            item = DealItem()
            item['website']='besmart'
            item['website_url'] = 'http://besmart.kz'

            raw_discount = clean_extract(
                deal, 
                'div.percent ::text',
            )
            item['discount'] = get_numbers_from_string(raw_discount)
            item['title'] = ''
            raw_summary_front = clean_extract(
                deal, 
                'div.title',
            )
            item['summary_front'] = drop_html_tags(raw_summary_front)
            raw_number_of_purchases = clean_extract(
                deal, 
                'div.sold-amount ::text',
            )
            item['number_of_purchases'] = get_numbers_from_string(raw_number_of_purchases)
            item['image_url'] = 'http://www.chocolife.me' + clean_extract(
                deal,
                'img.lazy-img ::attr(data-original)',
            )
            raw_old_price = clean_extract(
                deal,
                'div.real-price ::text',
            )
            item['old_price'] = get_numbers_from_string(raw_old_price)
            raw_new_price = clean_extract(
                deal,
                'div.discount-price span.big ::text',
            )
            item['new_price'] = get_numbers_from_string(raw_new_price)
            item['deal_url'] = 'http://www.besmart.kz' + clean_extract(
                deal,
                'div.title a ::attr(href)',
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
        item['conditions'] = clean_extract(
            sel,
            'div.deal-conditions div.star-list',
        )
        yield item
          
        
        

        

        





        



