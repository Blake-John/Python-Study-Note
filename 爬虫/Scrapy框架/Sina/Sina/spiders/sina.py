import scrapy
import os
from Sina.items import SinaItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com']
    start_urls = ['https://news.sina.com.cn/guide/']

    def parse(self, response):

        # 所有大类的标题和url
        parenttitle = response.xpath ("//div[@id='tab01']//h3/a/text ()").extract ()
        parenturl = response.xpath ("//div[@id='tab01']//h3/a/@href").extract ()

        # 所有小类的标题和url
        subtitle = response.xpath ("//div[@id='tab01']//ul[@class='list01']//a/text ()").extract ()
        suburl = response.xpath ("//div[@id='tab01']//ul[@class='list01']//a/@href").extract ()
        
        items = []

        # 爬取所有大类
        for i in range (0,len (parenttitle)) :
            parentfile = "Data/" + parenttitle[i]

            # 如果目录不存在，则创建目录
            if (not os.path.exists (parentfile)) :
                os.mkdir (parentfile)

            # 爬取所有小类
            for j in range (0,len (subtitle)) :
                item = SinaItem ()

                # 保存大类的title和url
                item['parentTitle'] = parenttitle[i]
                item['parentUrl'] = parenturl[i]

                # 很关键的一步：判断小类与大类的域名是否一致
                # 若结果返回 True 则将此内容放入当前文件夹中
                if_belong = suburl[j].startswith (parenturl[i])
                if if_belong :
                    subfilepath = parentfile + "/" + subtitle[j]
                    if (not os.path.exists (subfilepath)) :
                        os.mkdir (subfilepath)
                    
                    # 存储小类中各种字段数据
                    item['subUrl'] = suburl[j]
                    item['subTitle'] = subtitle[j]
                    item['subFilepath'] = subfilepath

                    items.append (item)
        
        for it in items :
            yield scrapy.Request (url=it['subUrl'],meta={'meta-1':it},callback=self.second_parse)
    

    def second_parse (self,response) :
        # 提取每次 Requests 返回的数据
        meta_1 = response.meta['meta-1']

        # 取出小类里的所有子链接
        sonurl = response.xpath ("//a/@href").extarct ()
        items = []
        for i in range (0,len (sonurl)) :
            # 检查每个链接是否以 大类url 开头，以 shtml 结尾，是则返回 True
            # if_belong = sonurl[i].startswith (meta_1['parentUrl']) and sonurl[i].endswith (".shtml")
            
            # # 如果属于本大类，获取字段值放在同一个item下便于传输
            # if if_belong :
            item = SinaItem ()
            item['parentTitle'] = meta_1['parentTitle']
            item['parentUrl'] = meta_1['parentUrl']
            item['subUrl'] = meta_1['subUrl']
            item['subTitle'] = meta_1['subTitle']
            item['subFilepath'] = meta_1['subFilepath']
            item['sub_SonUrl'] = sonurl[i] 

            items.append (item)

        for it in items :
            yield scrapy.Request (url=it['sub_SonUrl'],meta={'meta-2':it},callback=self.detail_parse)
    

    # 数据解析方法，获取文章标题和内容
    def detail_parse (self,response) :
        item = response.meta['meta-2']
        content = ""
        head = response.xpath ("//h1[@id='main_title']/text ()").extract ()
        content_list = response.xpath ("//div[@id='artibody']/p/text ()").extract ()
        for ct in content_list :
            content += ct
        
        item['head'] = head
        item['content'] = content

        yield item