from bs4.element import Script
import requests
from bs4 import BeautifulSoup
import re
import json

class CoronaVirusSpider (object) :
    def __init__ (self) :
        self.home_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
    
    def get_content_from_url (self,url) :
        """
        根据url，获取响应内容字符串数据
        :param url: 请求的url
        :return: 响应内容的字符串
        """
        response = requests.get (url)
        return response.content.decode ()
    
    def parse_home_page (self,home_page) :
        """
        解析首页内容，获取解析后的python数据
        :param home_page:首页的内容
        :return:解析后的python数据
        """
        soup = BeautifulSoup (home_page,"lxml")
        script = soup.find (id="getListByCountryTypeService2true")
        text = script.text
        json_str = re.findall (r"\[.+\]",text)[0]
        data = json.loads (json_str)
        return data
    
    def save (self,data,path) :
        with open (path,"w") as fp :
            json.dump (data,fp,ensure_ascii=False)

    def crawl_last_day_corona_virus (self) :
        """
        采集最近一天的疫情信息
        "return:
        """
        # 发送请求，获取首页内容
        home_page = self.get_content_from_url (self.home_url)
        # 解析首页内容，获取最近一天数据
        last_day_corona_virus = self.parse_home_page (home_page)
        # 保存数据
        self.save (last_day_corona_virus,"10111.json")

    def run (self) :
        self.crawl_last_day_corona_virus ()

if __name__ == "__main__" :
    spider = CoronaVirusSpider ()
    spider.run ()
        
