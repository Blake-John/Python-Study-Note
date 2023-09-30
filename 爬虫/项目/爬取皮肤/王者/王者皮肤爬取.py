import requests
import os

url = "https://pvp.qq.com/web201605/js/herolist.json"
herolist = requests.get (url) # 获取英雄列表json文件

herolist_json = herolist.json () #将获取的响应转化为json格式
hero_name = list (map (lambda x:x["cname"],herolist.json())) #提取英雄名字
hero_number = list (map (lambda x:x["ename"],herolist.json())) #提取英雄编号

# a = open ("D:/321123.txt","a")
# a.write (str (hero_name))
# a.write (str (hero_number))

def downloadimage () :
    os.mkdir ("D:/王者荣耀皮肤")
    i = 0
    for j in hero_number :
        os.chdir ("D:/王者荣耀皮肤")
        #创建文件夹
        os.mkdir (hero_name[i])
        #进入文件夹
        os.chdir (hero_name[i])
        i += 1
        for k in range (15) :
            #拼接url
            onehero_link = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/" + str (j) + "/" + str (j) + "-bigskin-" + str (k) + ".jpg"
            im = requests.get (onehero_link) #请求url
            if im.status_code == 200 :
                open (str (k) + ".jpg","wb").write (im.content) # 写入文件

downloadimage ()