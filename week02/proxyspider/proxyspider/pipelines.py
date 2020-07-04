# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class ProxyspiderPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'xdXD1986',
                       database = 'test',
                       charset = 'utf8mb4'
                        )

        # 获得cursor游标对象
        con1 = conn.cursor()
        values = (item['res_ip'],item['agent_ip'])
        con1.execute('INSERT INTO '+ 'test3' +' values(%s,%s)' ,values)
        conn.commit()
        #断开连接
        con1.close()
        conn.close()
        #return item
