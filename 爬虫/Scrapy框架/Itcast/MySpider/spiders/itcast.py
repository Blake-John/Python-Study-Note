import scrapy
from MySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath ("//div[@class='li_txt']")

        # 用来存储所有的 item字段
        items = []
        for node in node_list :
            # 创建 item字段对象，用来存储信息
            item = MyspiderItem ()

            # .extract () 将 xpath 对象转换为 Unicode字符串，但得到的仍为列表
            name = node.xpath ("./h3/text ()").extract ()
            title = node.xpath ("./h4/text ()").extract ()
            info = node.xpath ("./p/text ()").extract ()

            # 将数据类型转化为 "utf-8" 型式以便通过 管道 写入文档,这里是再在管道中再转换
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item