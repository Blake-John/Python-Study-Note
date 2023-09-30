from bs4 import BeautifulSoup

# BeautifulSoup 是一个可以从HTML或XML中提取数据的Python库
soup = BeautifulSoup ("<html>data</html>","lxml") # 解析文本
# BeautifulSoup对象：代表要解析整个文档树，它支持 遍历文档树 和 搜索文档树 中描述的大部分方法
# 使用BeautifulSoup需要指定一个解释器 "lxml"
print (soup) 
# BeautifulSoup会自动修正语法 "<html><body><p>data</p></body></html>"