import requests
import os
from bs4 import BeautifulSoup
import re

url = "https://pns.kurogame.com/image/list_2101_1.html"
response = requests.get (url)
# print (response.content.decode ())
body = response.content.decode () 
# 此时将网页编码使用 decode 解码成 unicode 编码
# a = open ("D:/12558.txt","w",encoding="utf-8")
# 指定新文件的编码 “utf-8” 使其符合网页编码
# a.write (body) # 将获取的响应写入文件，以便与查看            

soup = BeautifulSoup (body,"lxml")
# b = open ("D:/12559.txt","w",encoding="utf-8")
# b.write (str (soup))
pifuwangzhi = re.findall ('<li data-img="(.+)">',str (soup))
c = open ("D:/皮肤网址.txt","w",encoding="utf-8")
c.write (str (pifuwangzhi))
# mingzi = re.findall ("<p>(.+)</p>",str (soup))
# d = open ("C:/Users/123/OneDrive/桌面/学习/程序/爬虫/爬取皮肤/战双/皮肤名字.txt","w",encoding="utf-8")
# d.write (str (mingzi))
