# Python 的解释器在 导入模块 时，会：
# 1.搜索 当前目录 指定模块名的文件，如果有就直接导入
# 2.如果没有，再搜索 系统目录*
# > 在开发时，给文件起名，不要和 系统的模块文件 重名
# Python 中每一个模块都有一个内置属性 __file__ 可以 查看模块 的 完整路径

import random

print (random.__file__)

num = random.randint (0,10)
print (num)
