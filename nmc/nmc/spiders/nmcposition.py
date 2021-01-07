import scrapy
from nmc.items import MyItem

class NmcpositionSpider(scrapy.Spider):
    name = 'nmccrawl'
    city = 'chongqing'
    allowed_domains = ['http://www.nmc.cn/']
    start_urls = ['http://www.nmc.cn/publish/forecast/ACQ/chongqing.html/']
    
    def parse(self, response):
        item = MyItem()
        item['d'] = response.xpath('//*[@id="day7"]/div[1]/div/div[1]/text()[1]').extract()
        item['w'] = response.xpath('//*[@id="day7"]/div[1]/div/div[3]/text()').extract()
        item['c'] = 'chongqing'
        item['max_t'] = response.xpath('//*[@id="day7"]/div[1]/div/div[6]/text()').extract()
        item['min_t'] = response.xpath('//*[@id="day7"]/div[1]/div/div[7]/text()').extract()
        return item
