# 按行读取文件内容
# * read 方法默认会把文件的 所有内容 一次性读取到内存
# *如果文件太大，对内存的占用会非常严重
# readline 方法
# * readline 方法可以一次读取一行内容
# *方法执行后，会把 文件指针 移动到下一行，准备再次读取

# 读取大文件的正确姿势
# ```python
# # 打开文件
# file = open("README")

# while True:
#     # 读取一行内容
#     text = file.readline()

#     # 判断是否读到内容
#     if not text:
#         break

#     # 每读取一行的末尾已经有了一个 `\n`
#     print(text, end="")

# # 关闭文件
# file.close()
# ```

file = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme1.txt")
while True :
    text = file.readline ()
    if not text :
        break
    print (text)
file.close ()