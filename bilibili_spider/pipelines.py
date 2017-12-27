# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from bilibili_spider.items import UserItem, VideoItem
from bilibili_spider.database import db


class BilibiliSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class UserPipelines(object):
    def __init__(self):
        self.collection = db['User']

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            user_data = item['data']
            exist_user = self.collection.find_one({"mid": user_data['mid']})
            if exist_user is None:
                self.collection.insert(user_data)
        return item


class VideoPipelines(object):
    def __init__(self):
        self.collection = db['Video']

    def process_item(self, item, spider):
        if isinstance(item, VideoItem):
            exist_user = self.collection.find_one({"av": item['av']})
            if exist_user is None:
                self.collection.insert(dict(item))
        return item
