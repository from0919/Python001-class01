# -*- coding: utf-8 -*-
import scrapy
import json
from proxyspider.items import ProxyspiderItem

class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 通过ip查看请求的ip地址
    start_urls = ['http://httpbin.org/ip']
    # 通过header 查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        item = ProxyspiderItem()
        print(response.text)
        ip_detail_temp = eval(response.text)
        ip_detail_temp2 = ip_detail_temp['origin']
        ip_detail_list = ip_detail_temp2.split(',')

        item['res_ip'] = ip_detail_list[0].strip()
        item['agent_ip'] = ip_detail_list[1].strip()
        print(item['res_ip'])
        print(item['agent_ip'])
        yield item