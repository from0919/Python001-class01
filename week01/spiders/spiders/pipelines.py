# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        mv_dict ={}
        print("SpidersPipeline_begin")
        mvname = item['name']
        mvdate = item['date']
        mvtype = item['mv_type']
        
        mv_dict['name'] = mvname
        mv_dict['date'] = mvdate
        mv_dict['mv_type'] = mvtype
        movie_scrapy_maoyan = pd.DataFrame(mv_dict,index=[0])
        movie_scrapy_maoyan.to_csv('./movie_scrapy_maoyan.csv', encoding='gbk', mode='a', index=False, header=False)
        print("SpidersPipeline_end")
        return item
