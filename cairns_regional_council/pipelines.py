# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.log import INFO
import scraperwiki


class CairnsRegionalCouncilPipeline(object):
    def process_item(self, item, spider):
        unique_keys = ['council_reference']
        scraperwiki.sql.save(unique_keys, dict(item), table_name='data')
        spider.log("Saved {}".format(item['council_reference']), level=INFO)
