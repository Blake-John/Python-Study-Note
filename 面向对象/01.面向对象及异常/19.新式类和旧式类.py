# 新式类与旧式（经典）类
# > object 是 Python 为所有对象提供的 基类，提供有一些内置的属性和方法，可以使用 dir 函数查看
# * 新式类：以 object 为基类的类，推荐使用
# * 经典类：不以 object 为基类的类，不推荐使用

# * 在 Python 3.x 中定义类时，如果没有指定父类，会 默认使用 object 作为该类的 基类 Python 3.x 中定义的类都是 新式类
# * 在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类

# > 新式类 和 经典类 在多继承时 —— 会影响到方法的搜索顺序
# 为了保证编写的代码能够同时在 Python 2.x 和 Python 3.x 运行！
# 今后在定义类时，如果没有父类，建议统一继承自 object

# class 类名(object):
#     pass

class Animal (object) : # 新式类
    def run (self) :
        print ("The animal is running.")

class Dog (Animal) :
    def bark (self) :
        print ("The dog is barking.")

dog = Dog ()
dog.bark ()