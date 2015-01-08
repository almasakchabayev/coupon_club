# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DealItem(scrapy.Item):

   # ... other item fields ...
   image_url = scrapy.Field()
   title = scrapy.Field()
   summary_front=scrapy.Field()
   old_price=scrapy.Field()
   new_price = scrapy.Field()
   # end_timestamp = scrapy.Field()
   number_of_purchases = scrapy.Field()
   discount = scrapy.Field()
   # description = scrapy.Field()
   category = scrapy.Field()
   company=scrapy.Field()
   tag = scrapy.Field()
   deal_url = scrapy.Field()
   website = scrapy.Field()
   website_url = scrapy.Field()
   # address = scrapy.Field()
   conditions = scrapy.Field()
