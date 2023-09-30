import re
import requests
from bs4 import BeautifulSoup

# 发送请求，获取首页内容
response = requests.get ("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_page = response.content.decode ()
# print (home_page)
# 使用 BeautifulSoup 提取疫情数据
soup = BeautifulSoup (home_page,"lxml")
script = soup.find (id="getListByCountryTypeService2true")
print (script)
ctext = script.text


# 使用正则表达式提取json字符串
json_str = re.findall (r"\[.+\]",ctext)
print (json_str)