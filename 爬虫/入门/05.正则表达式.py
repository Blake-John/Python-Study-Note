# 正则表达式 是一种字符串匹配的模式
# 作用：
#  *检查一个字符串是否含有某种子串
#  *替换匹配的子串
#  *提取某个字符串中匹配的子串


import re

# 字符匹配
rs = re.findall ("abc","abcsghsfgsdfgc")
rs = re.findall ("a.c","a.cdfsjdclkfjsdf")
rs = re.findall ("a\.c","a.cdfsjdclkfjsdf")
rs = re.findall ("a.c","abcdfsjdclkfjsdf")
rs = re.findall ("a\.c","abcdfsjdclkfjsdf")
rs = re.findall ("a[bd]c","abcdfsjdclkfjsdf")

# 预定义字符集
#  .    匹配除换行符(\n)意外的所有字符
#  \d   数字：[0-9]
#  \D   非数字：[^\d]
#  \s   空白字符：[<空格>\t\r\n\f\v]
#  \S   非空白字符：[^\s]
#  \w   单词字符：[A-Za-z0-9_]
#  \W   非单词字符：[^\w]
# 数量词
#  *    匹配前一个字符0或无限次      abc* --> ab/abcc
#  +    匹配前一个字符1或无限次      abc+ --> abc/abcc
#  ?    匹配前一个字符0次或1次       abc? --> ab/abc
#  {m}  匹配前一个字符m次            abc{2} --> abcc

rs = re.findall ("\d","123")
print (rs)
rs = re.findall ("\w","12Az3_中文")
print (rs)