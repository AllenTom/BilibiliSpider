# BilibiliSpider
Bilibili的爬虫，使用scrapy
## 需求
1. python3.6
2. scrapy
3. pymongo
4. [scrapy_proxies](https://github.com/aivarsk/scrapy-proxies)
5. [scrapy-fake-useragent](https://github.com/alecxe/scrapy-fake-useragent)
## 爬取器
按需使用，以后会添加更多的爬取内容

*****
#### User(爬取用户）
```
scrapy crawl user
```
需要在settings中设置爬取的mid的起止点(USER_START和USER_END)
*****
#### Video(爬取视频信息）
```
scrapy crawl video
```
需要在settings中设置爬取的mid的起止点(VIDEO_START和VIDEO_END)
*****
## 使用配置
配置在setting中，配置相关信息
1. MongoDB数据库配置（连接参数）
2. scrapy的其他配置详见文档
3. [scrapy_proxies](https://github.com/aivarsk/scrapy-proxies)代理设置详见文档
## Licence(MIT)
```
MIT License

Copyright (c) 2017 AllenTom aka TakayamaAren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
