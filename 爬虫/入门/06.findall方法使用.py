import re

# findall方法，返回匹配的结果列表
rs = re.findall ("\d","chuan13zhi24")
print (rs)

# findall方法中，flag参数的使用
rs = re.findall ("a.bc","a\nbc",re.DOTALL)
print (rs)
rs = re.findall ("a.bc","a\nbc",re.S)
print (rs)

# API
# *re.findall (pattern,string,flags=0)
# *作用：扫描整个 string 字符串，返回所有与 pattern 匹配的列表
# *参数：
#    ** pattern：正则表达式
#    ** string：从此字符串中查找
#    ** flags：匹配模式
# *返回：
#    ** 返回 string 中与 pattern 匹配的结果列表
# *举例：re.findall ("\d","chuan13zhi24") --> ["1","3","2","4"]


#findall方法中分组的使用
rs = re.findall ("a.+bc","a\nbc",re.DOTALL)
print (rs) # ['a\nbc']
rs = re.findall ("a(.+)bc","a\nbc",re.DOTALL)
print (rs) # ['\n']   只返回小括号内的内容，小括号两边的字符用来定位