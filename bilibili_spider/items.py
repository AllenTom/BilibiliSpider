# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserItem(scrapy.Item):
    data = scrapy.Field()


class VideoItem(scrapy.Item):
    av = scrapy.Field()
    name = scrapy.Field()
    up = scrapy.Field()
    up_name = scrapy.Field()
    title = scrapy.Field()
    danmaku = scrapy.Field()
    reply = scrapy.Field()
    share = scrapy.Field()
    view = scrapy.Field()
    now_rank = scrapy.Field()
    his_rank = scrapy.Field()
    favorite = scrapy.Field()
    coin = scrapy.Field()
    create = scrapy.Field()
