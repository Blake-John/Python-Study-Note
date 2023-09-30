import requests
import os
import random


def Download () :
    a = int (input ("请输入爬取数量"))
    b = int (input ("请输入要爬取的最大值"))
    c = int (input ("请输入要爬取的最小值"))
    os.mkdir ("D:/猫图")
    os.chdir ("D:/猫图")
    for i in range (1,a + 1) :
        x = random.randint (c,b+1)
        respone = requests.get ("http://placekitten.com/g/" + str (x))
        if respone.status_code == 200 :
            a = open ("D:/猫图/%d.jpg" % i,"wb")
            a.write (respone.content)
        else :
            break

Download ()