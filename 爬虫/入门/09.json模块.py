# json 与 Python 数据类型关系
#  json            python
#  object          dict 
#  array           list
#  string          str
#  number(int)     int,long
#  number(real)    float
#  true            True
#  false           False
#  null            None
import json

json_str = """[{"provinceName":"美国","currentConfirmedCount":1179041
,"confirmedCount":1643499},{"provinceName":"英国","currentConfirmedCount":
222227,"confirmedCount":259559}]"""
print (json_str)
print (type (json_str)) # <class 'str'>
rs = json.loads (json_str) # "json.loads"把json字符串，转化为python数据
print (rs)
print (type (rs)) # <class 'list'>

# 把json格式文件，转化为Python类型的数据
with open ("C:/Users/123/OneDrive/桌面/学习/程序/爬虫/text.json") as fp :
    # 加载该文件对象，转化为python类型的数据
    python_list = json.load (fp) # "json.load"把json格式的文件对象转化为python类型数据
    print (python_list)
    print (type (python_list))