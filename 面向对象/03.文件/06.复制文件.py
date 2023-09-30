# 小文件复制
# *打开一个已有文件，读取完整内容，并写入到另外一个文件
# 大文件复制
# *打开一个已有文件，逐行读取内容，并顺序写入到另外一个文件

file = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme1.txt")
file2 = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme2.txt","w")

text = file.read ()
file2.write (text)

file.close ()
file2.close()



file3 = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme3.txt")
file4 = open ("C:/Users/Blake John/OneDrive/桌面/学习/程序/面向对象/03.文件/Readme4.txt","w")

while True :
    text = file3.readline ()
    if not text :
        break
    file4.write (text)

file3.close ()
file4.close()


