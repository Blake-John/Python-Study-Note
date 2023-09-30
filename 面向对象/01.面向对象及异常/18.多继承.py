# 多继承
# * 子类 可以拥有 多个父类，并且具有 所有父类 的 属性 和 方法

# 语法
# class 子类名(父类名1, 父类名2...)
#     pass

# # 多继承的使用注意事项
# *如果 不同的父类 中存在 同名的方法，子类对象 在调用方法时，会调用 哪一个父类中的方法呢？
# > 开发时，应该尽量避免这种容易产生混淆的情况！
#   如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承

# Python 中的 MRO —— 方法搜索顺序

# *Python 中针对 类 提供了一个 内置属性 __mro__ 可以查看 方法 搜索顺序
# *MRO 是 method resolution order，主要用于 在多继承时判断 方法、属性 的调用 路径

# 语法 
# print(C.__mro__) 注意：此处的 C 应为 继承的类 而非对象

# *在搜索方法时，是按照 __mro__ 的输出结果 从左至右 的顺序查找的
# *如果在当前类中 找到方法，就直接执行，不再搜索
# *如果 没有找到，就查找下一个类 中是否有对应的方法，如果找到，就直接执行，不再搜索
# *如果找到最后一个类，还没有找到方法，程序报错

class A :
    def test (self) :
        print ("A_test")
    def demo (self) :
        print ("A_demo")


class B :
    def demo (self) :
        print ("B_demo")
    def test (self) :
        print ("B_test")

class C (A,B) :
    def a (self) :
        self.test ()
        self.demo ()

c = C ()
c.a () 
print (C.__mro__)