import re

import operator
import scrapy
from classread.items import ClassreadItem

class CrSpider(scrapy.Spider):
    name = 'cr'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.49.01.12.00.00.html']

    # 基础页链接
    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):  # 爬取网站得到response后，自动回调parse方法
        # 基础xpath   //div//ul[@id="component_59"]/li
        li_list = response.xpath('//ul[@id="component_59"]/li')

        # 遍历
        for li in li_list:
            # 提取selector标签中的文字内容须在后面加上  .extract_first
            # 第一张图片和其他图片的标签属性不一样,一张图片的src可以直接爬取到，其他图片的路径则是在data-original下面
            src = li.xpath('.//img/@data-original').extract_first()
            # 判断获取的路径是否为None
            if src:
                src = 'http:' + src
            else:
                src = 'http:' + li.xpath('.//img/@src').extract_first()
            # 爬取
            name = li.xpath('.//img/@alt').extract_first()  # 书名
            press = li.xpath('.//span//a[@name="P_cbs"]/text()').extract_first()  # 出版社
            author = li.xpath('.//span[1]/a[1]/@title').extract_first()  # 作者
# 1经济管理类17， 2医学20， 3工学16， 4理学18， 5大学生素质教育15， 6文法类19， 7公共课04， 8农学12
#             b_id = "8"
            date = li.xpath('.//p[@class="search_book_author"]//span[2]/text()').extract_first()  # 出版时间
            b_href = 'http:' + li.xpath('./a[@class="pic"]/@href').extract_first()  # 点击图片进入详情页

            # 评论数
            results = li.xpath('.//p[@class="search_star_line"]//a/text()').extract_first()
            # 通过正则将 n条评论 中的n提取出来(n为数字)
            comment = re.findall(r"\d+\.?\d*", str(results))

            # 好评率   //ul[@id="component_59"]/li//p[@class="search_star_line"]/span//@style
            praises = li.xpath('.//p[@class="search_star_line"]/span//@style').extract_first()
            praise = re.findall(r"\d+\.?\d*", str(praises))

            # 价格    //ul[@id="component_59"]/li//p[@class="price"]/span[1]
            prices = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            price = re.findall(r"\d+\.?\d*", str(prices))

            # 学科id
            p_id = "8"

            print(src, name, press, author, date, b_href, comment, praise, price, p_id)  # 输出
            book = ClassreadItem(src=src, name=name, press=press, author=author, date=date, b_href=b_href,
                                 comment=comment, praise=praise, price=price, p_id=p_id)  #
            yield book

        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.49.01.12.00.00.html'
            yield scrapy.Request(url=url, callback=self.parse)

