import scrapy

class ClassreadItem(scrapy.Item):
    src = scrapy.Field()            # 图片链接
    name = scrapy.Field()           # 教材名称
    press = scrapy.Field()          # 出版社
    author = scrapy.Field()         # 作者
    date = scrapy.Field()           # 出版时间
    b_href = scrapy.Field()         # 详情页链接
    comment = scrapy.Field()        # 评论数
    praise = scrapy.Field()         # 好评率
    price = scrapy.Field()          # 价格
    p_id = scrapy.Field()           # 学科id

