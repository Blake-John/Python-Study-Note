import requests
import os
import random

def main () :
    position = input ("""请输入存放的位置：
如：D:/a/b,
注意！！！此文件夹不能存在""")
    a = input ("请输入要爬取的图片类型：\n1.正方形.2.自定义尺寸")
    if a == "1" :
        b = input ("请输入爬取类型：\n1.在某个范围内随机爬取.\n2.固定图片大小")
        if b == "1" :
            num = int (input ("请输入爬取数量"))
            max = int (input ("请输入要爬取的最大值"))
            min = int (input ("请输入要爬取的最小值"))
            os.mkdir (position)
            os.chdir (position)
            for i in range (1,num + 1) :
                x = random.randint (min,max+1)
                respone = requests.get ("http://placekitten.com/g/" + str (x))
                if respone.status_code == 200 :
                    a = open (position +"/%d.jpg" % i,"wb")
                    a.write (respone.content)
                else :
                    continue
        elif b == "2" :
            num = int (input ("请输入爬取数量"))
            max = input ("请输入要爬取的大小")
            os.mkdir (position)
            os.chdir (position)
            for i in range (1,num + 1) :
                respone = requests.get ("http://placekitten.com/g/" + max)
                if respone.status_code == 200 :
                    a = open (position + "/%d.jpg" % i,"wb")
                    a.write (respone.content)
                else :
                    continue
        else :
            print ("输入错误")
    elif a == "2" :
        num = int (input ("请输入爬取数量"))
        len = int (input ("请输入长："))
        wide = int (input ("请输入宽："))
        os.mkdir (position)
        os.chdir (position)
        for i in range (1,num + 1) :
            respone = requests.get ("http://placekitten.com/g/%d/%d" % (len,wide))
            if respone.status_code == 200 :
                a = open (position + "/%d.jpg" % i,"wb")
                a.write (respone.content)
            else :
                continue
    else :
        print ("输入错误")
        return


main ()