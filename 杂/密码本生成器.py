import itertools as its    #as 重命名
#迭代器
words="1234567890"
r=its.product (words,repeat=11)
#保存在文件中
dic=open ("11password.txt","a")
for i in r :
    #
    dic.write ("".join (i))
    dic.write ("".join ("\n"))
dic.close
