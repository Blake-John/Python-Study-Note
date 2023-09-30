# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:

    # 大类标题和url
    parentTitle = scrapy.Field()
    parentUrl = scrapy.Field()

    # 小类标题和子url
    subTitle = scrapy.Field()
    subUrl = scrapy.Field()

    # 小类目录存储路径
    subFilepath = scrapy.Field()

    # 小类下的子链接
    sub_SonUrl = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
    pass
