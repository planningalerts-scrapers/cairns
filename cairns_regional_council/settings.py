# -*- coding: utf-8 -*-

# Scrapy settings for orange_city_council project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'orange_city_council'

SPIDER_MODULES = ['orange_city_council.spiders']
NEWSPIDER_MODULE = 'orange_city_council.spiders'

ITEM_PIPELINES = {
    'orange_city_council.pipelines.OrangeCityCouncilPipeline': 500,
}

MEMDEBUG_ENABLED = True
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'morph.io orange_city_council (+http://morph.io)'
