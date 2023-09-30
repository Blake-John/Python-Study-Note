# find方法的作用：搜索文档树
# find (self,name = None,attrs = {},recursive = True,text = None,**kwargs)
# 参数
#   *name：标签名
#   *attrs：属性字典
#   *recursive：是否递归循环查找
#   *text：根据文本内容查找
# 返回
#   *查找到的第一个元素对象

import requests
from bs4 import BeautifulSoup

response = requests.get ("https://www.baidu.com") # 发送请求，获取响应
# response.content.decode ()  将获取的响应进行解码
soup = BeautifulSoup (response.content.decode (),"lxml") # 解析文本
title = soup.find_all ("a")
print (title)
title = soup.find ("title") # 从 soup 中查找
print (title)


# 根据属性进行查找
# 查找 id 为 link1 的标签
# 方法一：通过命名参数查找
a = soup.find (id = "link1")
print (a)
# 方法二：使用 attrs 来指定属性字典，进行查找
a = soup.find (attrs = {"id":"link1"})
print (a)
# 方法三：根据文本内容进行查找
text = soup.find (text = "Elsie")
print (text)


# Tag对象：应用于原始文档中的XML和HTML标签，可用 遍历文档树 和 搜索文档树 以及获取标签内容
# 属性：
#   *name：获取标签名称
#   *attrs：获取标签所有属性的键和值
#   *text：获取标签的文本字符串
print (type (title)) # <class 'bs4.element.ResultSet'>
print ("标签名",title.name)
print ("标签所有属性",title.attrs)
print ("标签文本内容",title.text)