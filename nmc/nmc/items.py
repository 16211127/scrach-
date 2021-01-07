# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyItem(scrapy.Item):

    w = scrapy.Field()
    d = scrapy.Field()
    c = scrapy.Field()
    max_t = scrapy.Field()
    min_t = scrapy.Field()
    #依次为天气，日期，城市，最大温度和最小温度
