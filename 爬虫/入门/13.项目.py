# send a request and get a response
# get data from the first page
# get json from the data
# change json into python
# save the data in json format

import requests
from bs4 import BeautifulSoup
import re
import json

response = requests.get ("https://ncov.dxy.cn/ncovh5/view/pneumonia")
home_page = response.content.decode ()
# print (home_page)
soup = BeautifulSoup (home_page,"lxml")
script = soup.find (id="getListByCountryTypeService2true")
text = script.text
# print (script)
json_str = re.findall (r"\[.+\]",text)
# print (json_str)
last_day_corona_virus = json.loads (str (json_str))
# print (last_day_corona_virus)
with open ("C:/Users/123/OneDrive/桌面/学习/程序/爬虫/text0.json","w") as fp :
    json.dump (last_day_corona_virus,fp,ensure_ascii=False)