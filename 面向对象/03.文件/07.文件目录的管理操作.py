# 文件/目录的常用管理操作
# *在 终端/文件浏览器、 中可以执行常规的 文件/目录 管理操作，例如：
#   *创建、重命名、删除、改变路径、查看目录内容、……
# *在Python中，如果希望通过程序实现上述功能，需要导入 os 模块

# 文件操作
# | 序号 | 方法名 | 说明       | 示例                            |
# | ---- | ------ | --------- | ------------------------------ |
# | 01   | rename | 重命名文件 | os.rename(源文件名, 目标文件名)  |
# | 02   | remove | 删除文件   | os.remove(文件名)               |

# 目录操作
# | 序号 | 方法名     | 说明           | 示例                   |
# | ---- | ---------- | -------------- | --------------------- |
# | 01   | listdir    | 目录列表       | os.listdir(目录名)     |
# | 02   | mkdir      | 创建目录       | os.mkdir(目录名)       |
# | 03   | rmdir      | 删除目录       | os.rmdir(目录名)       |
# | 04   | getcwd     | 获取当前目录   | os.getcwd()            |
# | 05   | chdir      | 修改工作目录   | os.chdir(目标目录)      |
# | 06   | path.isdir | 判断是否是文件 | os.path.isdir(文件路径) |

# > 提示：文件或者目录操作都支持 相对路径 和 绝对路径

import os 
a = os.listdir ("C:/Users/Blake John/OneDrive/桌面/学习/程序")
print (a)
os.rename ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme5.txt","C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme4.txt")
