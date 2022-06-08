# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import urllib

import pymysql
from itemadapter import ItemAdapter

from classread import settings


class ClassreadPipeline:
    # 在爬虫文件开始前，执行此方法，将文件打开
    def open_spider(self, spider):
        print("------爬取开始------")
        self.fp = open('books.json', 'w', encoding='utf-8')
    # item就是yield后面的book对象
    def process_item(self, item, spider):
        # 向文件中写入内容
        self.fp.write(str(item))
        return item
    # 在爬虫文件结束后，执行此方法，将文件关闭
    def close_spider(self, spider):
        self.fp.close()
        print("------爬取结束------")

import urllib.request
# 多条管道开启
# class DangDownLoadPipeline:
#     def process_item(self, item, spider):
#         # 下载图片d到指定文件夹  在路径前添加 http:
#         url = 'http:' + item.get('src')
#         filename = './books/' + item.get('name') + '.jpg'
#         urllib.request.urlretrieve(url=url, filename=filename)
#         return item

class DBPipeline:
    # ==========================================================
    def __init__(self):
        # 链接数据库
        self.connect = pymysql.connect(host=settings.MYSQL_HOST,
                                       port=3306,
                                       user=settings.MYSQL_USER,
                                       passwd=settings.MYSQL_PASSWD,
                                       db=settings.MYSQL_DBNAME,
                                       charset='utf8',
                                       use_unicode=True)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 插入数据
        try:
            name = item.get("name", "N/A")          # 有的图书有数据项缺失，这里做了容错处理
            author = item.get("author", "N/A")      # 作者
            src = item.get("src", "N/A")            # 图片链接
            press = item.get("press", "N/A")        # 出版社
            date = item.get("date", "N/A")          # 出版时间
            b_href = item.get("b_href", "N/A")      # 详情页链接
            comment = item.get("comment", "N/A")    # 评论数
            praise = item.get("praise", "N/A")      # 好评率
            price = item.get("price", "N/A")        # 价格
            p_id = item.get("b_id", "8")                 # 学科id

            sql = "insert into bookclass_tbook(name, author, src, press, date, b_href, comment, praise, price, p_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (name, author, src, press, date, b_href, comment, praise, price, p_id))  #
            self.connect.commit()  # 提交
        except Exception as e:
            # 出现错误时打印错误日志
            print(e)
        return item

    def close_spider(self, spider):  # 关闭数据库
        self.cursor.close()
        self.connect.close()
    # ==============================================================
