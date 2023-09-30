import requests
import re
from bs4 import BeautifulSoup
import os
def Download () :
    url = "https://www.silukew.com/ny78343/"
    respone = requests.get (url)
    body = respone.content.decode ()
    # os.mkdir ("D:/第一序列")
    # os.chdir ("D:/第一序列")
    # a = open ("D:/第一序列/123.txt","w")
    # a.write (body)
    if not os.path.exists ("D:/夜的命名术") :
        os.mkdir ("D:/夜的命名术")

    # 爬取小说页面地址
    html = re.findall ("<dd><a href=\"(.+)\"  >",body)
    # b = open ("D:/第一序列/html.txt","w")
    # b.write (str (html))

    # 爬取小说标题
    title = re.findall ("<dd><a href=.+>(.+)</a></dd>",body)
    # c = open ("D:/第一序列/title.txt","w")
    # c.write (str (title))
    
    # 开始下载
    for j in html :
        respone2 = requests.get ("https://www.silukew.com" + j)
        context = respone2.content.decode ()
        # d = open ("D:/第一序列/content.txt","w")
        # d.write (str (context))
        content = re.findall ("&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br><br>",context)
        # print (str (content))
        x = html.index (j)
        txt = open ("D:/夜的命名术/" + title[x] + ".txt","a")
        txt.write ("\n")
        txt.write (title[x])
        txt.write ("\n")
        for i in content :
            txt.write ("    ")
            txt.write (i)
            txt.write ("\n")

Download ()