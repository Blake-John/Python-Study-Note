import re

# 在不使用r原串的时候，处理转义符
rs = re.findall ("a\nbc","a\nbc")
print (rs)
rs = re.findall ("a\\\nbc","a\nbc")
print (rs)

#r原串在正则中可以消除转义符带来的影响
rs = re.findall (r"a\nbc","a\nbc")
print (rs)

#扩展：可以解决写正则的时候，不符合PEP8规范的问题
rs = re.findall (r"\d","a123")
print (rs)