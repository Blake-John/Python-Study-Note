# 1.子类对象 不能 在自己的方法内部，直接 访问 父类的 私有属性 或 私有方法
# 2.子类对象 可以通过 父类 的 公有方法 间接 访问到 私有属性 或 私有方法
# >私有属性、方法 是对象的隐私，不对外公开，外界 以及 子类 都不能直接访问
# >私有属性、方法 通常用于做一些内部的事情

class A :
    def  __init__(self) -> None:
        self.num1 = 100
        self.__num2 = 200
    def __test (self) :
        print ("Private method %d %d " % (self.num1,self.__num2))


class B (A) :
    def demo (self) :
        # 访问父类的私有属性
        # print ("Acess the father class's attribute %d " % self.__num2)
        # 调用父类的私有方法
        # self.__test ()
        pass

b = B ()
print (b)
# 在外界不能直接访问对象的私有属性/调用私有方法
# print (b.__num2)
# b.test ()
b.demo ()