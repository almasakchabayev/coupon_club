from datetime import datetime
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from coupon_scraper.items import MyItem


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
        category_urls = sel.xpath('//ul[@class="b-deals__menunav__select"]/li/a/@href').extract()
        for url in category_urls[1:8]:
            if 'http' not in url:
                url = 'http://www.chocolife.me' + url
            yield Request(url, callback=self.parse_deal)

    def parse_deal(self, response):
        sel = Selector(response)
        deals=sel.xpath('//li[@class="b-deal"]')
        count=0

        for deal in deals[:10]:
            if 'display: none' not in deal.xpath('//@style').extract()[0]:
                item=MyItem()
                item['discount_text']=sel.xpath('//span[@class="e-deal__discount"]/text()').extract()[count]
                item['title']=sel.xpath('//h2[@class="e-deal__title"]/text()').extract()[count]
                item['summary_front']=sel.xpath('//p[@class="e-deal__text"]/text()').extract()[count]
                item['a_number_of_purchases']=sel.xpath('//span[@class="e-deal__link"]/text()').extract()[count]
                item['image_url']='http://www.chocolife.me'+sel.xpath('//img[@class="e-deal__img lazy"]/@data-original').extract()[count]
                item['old_price']=sel.xpath('//span[@class="e-deal__price e-deal__price--old "]/text()').extract()[count]
                item['new_price']=sel.xpath('//span[@class="e-deal__price "]/text()').extract()[count]
                item['deal_url']=sel.xpath('//a[@class="e-link--deal"]/@href').extract()[count]
                count+=1
                request = Request(
                    item['deal_url'],
                    callback=self.parse_deal_info
                )
                request.meta['item'] = item
                yield request

    def parse_deal_info(self, response):
        item = response.meta['item']
        sel = Selector(response)
        item['address']=sel.xpath('//li[@class="e-offer__feature "]/text()').extract()[0]
        item['info']=sel.xpath('//p[@class="e-offer__description"]/text()').extract()[0]
        yield item