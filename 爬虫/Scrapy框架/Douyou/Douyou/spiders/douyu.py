import scrapy
import json
from Douyou.items import DouyouItem

class DouyouSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_urls = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_urls + str (offset)]

    def parse(self, response):
        data_list = json.loads (response.body)['data']
        
        for data in data_list :
            item = DouyouItem ()
            item['name'] = data['nickname']
            item['image'] = data['vertical_src']
            
            yield item

            
            