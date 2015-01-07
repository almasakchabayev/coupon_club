# -*- coding: utf-8 -*-

# Scrapy settings for coupon_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import os
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DJANGO_BASE_DIR = os.path.join(PROJECT_DIR, 'coupon_club')
sys.path.insert(0, DJANGO_BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'coupon_club.settings'
BOT_NAME = 'coupon_scraper'

SPIDER_MODULES = ['coupon_scraper.spiders']
NEWSPIDER_MODULE = 'coupon_scraper.spiders'

ITEM_PIPELINES = {
    'coupon_scraper.pipelines.CouponScraperPipeline': 500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'coupon_scraper (+http://www.yourdomain.com)'
