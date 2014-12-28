from datetime import datetime
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from arbitrage_scraper.items import FootballMatchContainerItem


class ArbitrageOddsSpider(Spider):
    name = "arbitrage"
    allowed_domains = [
        'chocolife.me'
    ]
    start_urls = [
        'http://www.chocolife.me'
    ]

    def parse(self, response):
        selector = Selector(response)