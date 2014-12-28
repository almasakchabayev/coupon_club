# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Person
