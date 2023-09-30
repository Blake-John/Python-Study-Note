# 捕获未知错误
# *在开发时，要预判到所有可能出现的错误，还是有一定难度的
# *如果希望程序 无论出现任何错误，都不会因为Python解释器 抛出异常而被终止，可以再增加一个 except

# 语法如下：
# except Exception as result:
#     print("未知错误 %s" % result)

# 异常捕获的完整语法：
# try:
#     # 尝试执行的代码
#     pass
# except 错误类型1:
#     # 针对错误类型1，对应的代码处理
#     pass
# except 错误类型2:
#     # 针对错误类型2，对应的代码处理
#     pass
# except (错误类型3, 错误类型4):
#     # 针对错误类型3 和 4，对应的代码处理
#     pass
# except Exception as result:
#     # 打印错误信息
#     print(result)
# else:
#     # 没有异常才会执行的代码
#     pass
# finally:
#     # 无论是否有异常，都会执行的代码
#     print("无论是否有异常，都会执行的代码")

from typing import Final


try :
    num = int (input ("Please input a integer:"))
    a = 8 / num
    print (a)
except ValueError :
    print ("Please input a integer,not other types of value.")
except Exception as result :
    print ("%s" % result)
else :
    print ("Normal execution.")
finally :
    print ("Code execution complete.")