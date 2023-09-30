import scrapy
from Punish.items import PunishItem

class PunishSpider(scrapy.Spider):
    name = 'punish'
    allowed_domains = ['bilibili.com']
    base_urls = 'https://search.bilibili.com/all?keyword=%E6%88%98%E5%8F%8C&from_source=webtop_search&spm_id_from=333.5/&page='
    page = 1
    start_urls = [base_urls + str (page)]

    def parse(self, response):
        print ("*" * 50)
        node_list = response.xpath ("//li[@class='video-item matrix']")

        for node in node_list :
            print ("*" * 50)

            item = PunishItem ()

            html = node.xpath ("./a/@href").extract ()
            title = node.xpath ("./a/@title").extract ()      
            view_count = node.xpath (".//span[@title='观看']//text ()").extract ()
            barrage = node.xpath (".//span[@title='弹幕']//text ()").extract ()
            time = node.xpath (".//span[@title='上传时间']//text ()").extract ()
            up = node.xpath (".//span[@title='up主']//text ()").extract ()

            item['html'] = html[0]
            item['title'] = title[0]
            item['view_count'] = view_count[0]
            item['barrage'] = barrage[0]
            item['time'] = time[0]
            item['up'] = up[0]

            yield item
        
        if self.page < 50 :
            self.page += 1
            url = self.base_urls + str (self.page)
            yield scrapy.Request (url,callback=self.parse)