# -*- coding: utf-8 -*-
import json
import random

import datetime
import re

import scrapy
import time
from scrapy import Request, Selector
from scrapy.conf import settings
from scrapy.http import Response

from bilibili_spider.items import VideoItem


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['bilibili.com']
    start_urls = ['http://bilibili.com/']
    spider_av = range(settings.get("VIDEO_START"), settings.get("VIDEO_END"))

    def start_requests(self):
        for av in self.spider_av:
            video_header = {
                "Host": "www.bilibili.com",
                "Accept": "text/html,application",
                'Accept-Language': 'en-US,en;q=0.5',
            }
            print(f'爬取 av{av}')
            video_request = Request(
                url=f'https://www.bilibili.com/video/av{av}',
                headers=video_header,
                callback=self.parse_video_page
            )
            yield video_request

    def parse(self, response: Response):
        item = response.request.meta['item']
        data = json.loads(response.body)['data']
        item['view'] = data['view']
        item['danmaku'] = data['danmaku']
        item['reply'] = data['reply']
        item['favorite'] = data['favorite']
        item['coin'] = data['coin']
        item['share'] = data['share']
        item['now_rank'] = data['now_rank']
        item['his_rank'] = data['his_rank']
        return item

    def parse_video_page(self, response: Response):
        item = VideoItem()
        root_selector: Selector = Selector(response=response)
        if root_selector.xpath('//title/text()').extract_first() == '哔哩哔哩 (゜-゜)つロ 干杯~-bilibili':
            return
        item['name'] = root_selector.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/h1/text()").extract_first()
        item['up_name'] = root_selector.xpath(
            '//*[@id="viewbox_report"]/div[2]/div[2]/div[1]/a[1]/text()').extract_first()
        mid_link: str = root_selector.xpath('//*[@id="viewbox_report"]/div[2]/div[2]/div[1]/a[1]/@href').extract_first()
        item['up'] = int(mid_link.replace('//space.bilibili.com/', ""))
        av = response.url.replace("https://www.bilibili.com/video/av", "")
        item['av'] = av.replace("/", "")
        create = root_selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[3]/time/i/text()').extract_first()

        item['create'] = create

        timestamp = int(round(time.time() * 1000))
        random_plus = timestamp + random.randint(380, 430)
        random_jq = random.randint(3057370, 9999999)
        header = {
            'Referer': f'https://www.bilibili.com/video/av{item["av"]}/',
            'Host': 'api.bilibili.com',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        yield Request(
            url=f'http://api.bilibili.com/archive_stat/stat?callback=&aid={item["av"]}&type=json&_={timestamp}',
            dont_filter=False,
            headers=header,
            callback=self.parse,
            meta={"item": item}
        )
