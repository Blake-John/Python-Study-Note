# 继承的概念：子类 拥有 父类 的所有 方法 和 属性
# 继承的语法
# class 类名(父类名):
#     pass

# *子类 继承自 父类，可以直接 享受 父类中已经封装好的方法，不需要再次开发
# *子类 中应该根据 职责，封装 子类特有的 属性和方法

# 专业术语
# * Dog 类是 Animal 类的 子类，Animal 类是 Dog 类的 父类，Dog 类从 Animal 类 继承
# * Dog 类是 Animal 类的 派生类，Animal 类是 Dog 类的 基类，Dog 类从 Animal 类 派生

# 继承的传递性
# * C 类从 B 类继承，B 类又从 A 类继承
# *那么 C 类就具有 B 类和 A 类的所有属性和方法

class Animal :
    def eat (self) :
        print ("Eat")
    def drink (self) :
        print ("Drink")
    def run (self) :
        print ("Run")
    def sleep () :
        print ("Sleep")


class Dog (Animal) :
    # def eat (self) :
    #     print ("Eat")
    # def drink (self) :
    #     print ("Drink")
    # def run (self) :
    #     print ("Run")
    # def sleep (self) :
    #     print ("Sleep")
    def bark (self) :
        print ("Wangwangwang!!!")


class XiaoTianQuan (Dog) :
    def fly (self) :
        print ("I can fly.")
wangcai = Dog ()
xiaotian = XiaoTianQuan ()

wangcai.eat ()
wangcai.run ()
wangcai.bark ()
xiaotian.drink () # 继承的传递性
xiaotian.bark ()
xiaotian.fly ()