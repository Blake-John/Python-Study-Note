import requests
import re
from bs4 import BeautifulSoup
import json

url = "http://www.cntour.cn"
response = requests.get (url)
soup = BeautifulSoup (response.text,"lxml")
# print (soup)
title = soup.find ("title")
print (title)
a = soup.find ("a")
print (a)
text = open ("C:/Users/123/OneDrive/桌面/学习/程序/爬虫/1.txt","a")
text.write (str (title))
text.write (str (a))
text.close ()