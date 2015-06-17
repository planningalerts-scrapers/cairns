# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DevelopmentApplicationItem(scrapy.Item):
    council_reference = scrapy.Field()
    date_received = scrapy.Field()
    date_scraped = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    info_url = scrapy.Field()
    comment_url = scrapy.Field()
    external_reference = scrapy.Field()

