# read 方法 —— 读取文件
# * open 函数的第一个参数是要打开的文件名（文件名区分大小写）
#   *如果文件 存在，返回 文件操作对象
#   *如果文件 不存在，会 抛出异常
# * read 方法可以一次性 读入 并 返回 文件的 所有内容
# * close 方法负责 关闭文件
#   *如果 忘记关闭文件，会造成系统资源消耗，而且会影响到后续对文件的访问
# *注意：read 方法执行后，会把 文件指针 移动到 文件的末尾

# ```python
# # 1. 打开 - 文件名需要注意大小写
# file = open("README")
# # 2. 读取
# text = file.read()
# print(text)
# # 3. 关闭
# file.close()
# ```

# 提示
# *在开发中，通常会先编写 打开 和 关闭 的代码，再编写中间针对文件的 读/写 操作！

# 文件指针（知道）
# *文件指针 标记 从哪个位置开始读取数据
# *第一次打开 文件时，通常 文件指针会指向文件的开始位置
# *当执行了 read 方法后，文件指针 会移动到 读取内容的末尾
#   *默认情况下会移动到 文件末尾

# 打开文件
file = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/README.txt")
# 读取文件内容
text = file.read ()
print (text)
print (len (text))
print ("-" * 50)
text = file.read ()
print (text)
print (len (text))
# 关闭文件
file.close ()