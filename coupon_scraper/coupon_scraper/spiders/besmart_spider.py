from datetime import datetime
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from coupon_scraper.items import DealItem

from coupon_scraper.spiders.utils import clean_extract, get_numbers_from_string

def clean_extract(some_selector,xpath_of_info):
    try:
        clean_value_list = some_selector.xpath(xpath_of_info).extract()
        i=0
        clean_value=''
        for i in range(0, len(clean_value_list)):
            
            clean_value=clean_value+clean_value_list[i]
            i+=1
    except:
        clean_value = ''
    return clean_value


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
            item['discount']=clean_extract(deal,'.//div[@class="percent"]/text()')
            
            item['title']=""
            item['summary_front']=clean_extract(deal,'.//div[@class="title"]/a/text()')
            item['number_of_purchases']=clean_extract(deal,'.//div[@class="sold-amount"]/text()')
            item['image_url']='http://www.besmart.kz'+ deal.xpath('.//img[@class="lazy-img"]/@data-original').extract()[0]
            item['old_price']=clean_extract(deal,'.//div[@class="real-price"]/text()')
            
            item['new_price']=clean_extract(deal,'.//span[@class="big"]/text()')
            item['deal_url']='http://www.besmart.kz'+ deal.xpath('.//div[@class="title"]/a/@href').extract()[0]
            
            request = Request(
                item['deal_url'],
                callback=self.parse_deal_info
            )
            request.meta['item'] = item
            yield request

    def parse_deal_info(self, response):
        item = response.meta['item']
        sel = Selector(response)
        sel_one=sel.xpath('//div[@class="deal-left star-list"]')
        sel_two=sel.xpath('//div[@class="contacts large"]')
        item['info']=clean_extract(sel_one,'.//span/text()')
        item['address']=clean_extract(sel_two,'.//li/text()')
        yield item
          
        
        

        

        





        



