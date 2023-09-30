# *在程序执行时，可能会遇到 不同类型的异常，并且需要 针对不同类型的异常，做出不同的响应，这个时候，就需要捕获错误类型了

# *语法如下：
# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except (错误类型2, 错误类型3):
#     # 针对错误类型2 和 3，对应的代码处理
#     pass
# except Exception as result:
#     print("未知错误 %s" % result)

# * 当 Python 解释器 抛出异常 时，最后一行错误信息的第一个单词，就是错误类型


try :
    num = int (input ("Please input a integer:"))
    result = 8 / num
    print (result)
except ZeroDivisionError :
    print ("The divisor can't be 0.")
except ValueError :
    print ("Please input a integer,not other types of value.")