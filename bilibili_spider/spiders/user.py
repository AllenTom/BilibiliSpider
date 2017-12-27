# -*- coding: utf-8 -*-
import datetime
import json
import random
import time
from imp import reload

import scrapy
import sys
from scrapy import FormRequest
from scrapy.conf import settings
from scrapy.http import Response

from bilibili_spider.items import UserItem


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))

    return current_milli_time()


class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['bilibili.com']
    start_urls = []
    spider_user_uid = range(settings.get("USER_START"), settings.get("USER_END"))

    def start_requests(self):
        for uid in self.spider_user_uid:
            header = {
                'Referer': 'https://space.bilibili.com/' + str(uid),
                'Origin': 'http://space.bilibili.com',
                'Host': 'space.bilibili.com',
                'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
            }
            body = {
                '_': str(datetime_to_timestamp_in_milliseconds(datetime.datetime.now())),
                'mid': str(uid)
            }
            print(f'Create User Mid {uid}')
            yield FormRequest(
                url='http://space.bilibili.com/ajax/member/GetInfo',
                dont_filter=False,
                headers=header,
                formdata=body,
                callback=self.parse
            )

    def parse(self, response: Response):
        data = json.loads(response.body)
        item = UserItem()
        item['data'] = data['data']
        return item
