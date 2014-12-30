# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):

   # ... other item fields ...
   image_url = scrapy.Field()
   title = scrapy.Field()
   summary_front=scrapy.Field()
   old_price=scrapy.Field()
   new_price = scrapy.Field()
   end_date_time = scrapy.Field()
   a_number_of_purchases = scrapy.Field()
   discount_percentage = scrapy.Field()
   discount_text = scrapy.Field() #up to, from, etc.
   description = scrapy.Field()
   category = scrapy.Field()
   company=scrapy.Field()
   tag = scrapy.Field()
   deal_url = scrapy.Field()
   website = scrapy.Field()
   address = scrapy.Field()
   info = scrapy.Field()
