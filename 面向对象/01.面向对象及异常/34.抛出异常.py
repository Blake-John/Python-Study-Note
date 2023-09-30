# *在开发中，除了 代码执行出错Python解释器会 抛出 异常之外
# *还可以根据 应用程序 特有的业务需求 主动抛出异常

# *Python中提供了一个 Exception 异常类
# *在开发时，如果满足 特定业务需求时，希望 抛出异常，可以：
#   1.创建 一个 Exception 的 对象
#   2.使用 raise 关键字 抛出 异常对象


def input_password () :
    password = input ("Please input your password:")
    if len (password) >= 8 :
        return password
    print ("Throw a exception.")
    # 创建异常对象 - 可以使用错误信息字符串作为参数
    ex = Exception ("The lenth of the password is not enough.")
    # 主动抛出异常
    raise ex

try :
    print (input_password ())
except Exception as result :
    print (result)