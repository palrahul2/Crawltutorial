# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import _sqlite3

class CrawltutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = _sqlite3.connect("mycrawls.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS crawls_tb""")
        self.curr.execute(""" create table crawls_tb(
                    actorname text,
                    per_traits varchar,
                   actor_img varchar
                   
                      )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into crawls_tb values (?,?,?)""",(
            item['actorname'][0],
            item['per_traits'][0],
            item['actor_img'][0]
        ))
        self.conn.commit()








