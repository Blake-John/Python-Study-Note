import requests
import os
import random


def Download () :
    a = int (input ("请输入爬取数量"))
    b = int (input ("请输入要爬取的长"))
    c = int (input ("请输入要爬取的宽"))
    os.mkdir ("D:/a")
    os.chdir ("D:/a")
    for i in range (1,a + 1) :
        respone = requests.get ("http://placekitten.com/g/%d/%d" % (b,c))
        if respone.status_code == 200 :
            a = open ("D:/a/%d.jpg" % i,"wb")
            a.write (respone.content)
        else :
            break

Download ()