import requests

response = requests.get ("https://ncov.dxy.cn/ncovh5/view/pneumonia")
# response.encoding = "utf-8"   utf-8为一种可变长度字符编码
# print (response.text)
print (response.content.decode ()) 
# content将数据转化为二进制，decode将二进制解码

# response.text：响应体str类型
# response.encoding：二进制转换字符使用的编码
# response.content：响应体bytes类型


# 打印所使用的编码：ISO-8859-1
# print (response.encoding)
# 设置编码为：UTF-8/utf-8
# response.encoding = "utf-8"
# print (response.text)
