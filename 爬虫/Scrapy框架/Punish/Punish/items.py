# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PunishItem(scrapy.Item):
    # define the fields for your item here like:
    html = scrapy.Field()
    title = scrapy.Field ()
    view_count = scrapy.Field ()
    barrage = scrapy.Field ()
    time = scrapy.Field ()
    up = scrapy.Field ()
    pass
