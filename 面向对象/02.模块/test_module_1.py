def say_hello () :
    print ("I'm module one.")

class Dog (object) :
    pass


if __name__ == "__main__" :
    # 直接执行的代码不是向外界提供的工具
    print ("The code by Blake John.")
    # 文件被导入时，能够直接执行的代码不需要被执行
    say_hello ()

    # 如果直接执行模块，__mian__
    # 如果作为导入，则为 模块名
    print (__name__)