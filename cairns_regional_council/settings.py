# -*- coding: utf-8 -*-

# Scrapy settings for cairns_regional_council project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'cairns_regional_council'

SPIDER_MODULES = ['cairns_regional_council.spiders']
NEWSPIDER_MODULE = 'cairns_regional_council.spiders'

ITEM_PIPELINES = {
    'cairns_regional_council.pipelines.CairnsRegionalCouncilPipeline': 500,
}

MEMDEBUG_ENABLED = True
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'morph.io cairns_regional_council (+http://morph.io)'
