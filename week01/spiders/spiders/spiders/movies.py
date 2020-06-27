# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import re
from spiders.items import SpidersItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

#    def parse(self, response):
#        pass

   

    # 解析函数
    def parse(self, response):
        # 打印网页的url
        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        print('----0')
        print(len(movies))
        cookies = {
                    'uuid': '66a0f5e7546b4e068497.1542881406.1.0.0',
                    '_lxsdk_cuid': '1673ae5bfd3c8-0ab24c91d32ccc8-143d7240-144000-1673ae5bfd4c8',
                    '__mta': '222746148.1542881402495.1542881402495.1542881402495.1',
                    'ci': '20',
                    'rvct': '20%2C92%2C282%2C281%2C1',
                    '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
                    '_lxsdk_s': '1674f401e2a-d02-c7d-438%7C%7C35'}

        for i in range(10):
            item = SpidersItem()
            link = movies[i].xpath('./a/@href').extract_first()
            print('----1')
            print(link)
            print('----2')
            link = "https://maoyan.com" + link
            print(link)
            yield scrapy.Request(url=link, meta={'item': item}, cookies=cookies,callback=self.parse2)
    
    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        print('----3')
        print(response)
        movie_detail = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        #print(movie_detail)
        print('----3')
        movie_name = movie_detail.xpath('./h1/text()').extract_first().strip()
        movie_date = movie_detail.xpath('./ul/li[3]/text()').extract_first().strip()
        movie_type_detail = movie_detail.xpath('./ul/li[1]/a/text()')
        movie_type = ''
        for one in movie_type_detail:
            print('----4')
            movie_type_temp = one.extract().strip()
            if movie_type == "":
                movie_type = movie_type_temp
            else:
                movie_type = movie_type + "," + movie_type_temp
            #print(movie_type)
        movie_date = re.search(r'(\S+\d)',movie_date).group()
        item['name'] = movie_name
        item['date'] = movie_date
        item['mv_type'] = movie_type
        yield item



