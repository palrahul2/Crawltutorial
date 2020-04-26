# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawltutorialItem(scrapy.Item):
    # define the fields for your item here like:
    actorname = scrapy.Field()
    per_traits = scrapy.Field()
    actor_img = scrapy.Field()

