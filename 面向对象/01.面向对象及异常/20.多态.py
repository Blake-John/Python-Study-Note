# 面向对象三大特性

# 1.封装 根据 职责 将 属性 和 方法 封装 到一个抽象的 类 中
#   *定义类的准则 

# 2.继承 实现代码的重用，相同的代码不需要重复的编写
#   *设计类的技巧 
#   *子类针对自己特有的需求，编写特定的代码

# 3.多态 不同的 子类对象 调用相同的 父类方法，产生不同的执行结果
#   *多态 可以 增加代码的灵活度
#   *以 继承 和 重写父类方法 为前提
#   *是调用方法的技巧，不会影响到类的内部设计

class Dog (object) :
    def __init__(self,name) -> None:
        self.name = name
    def game (self) :
        print ("%s jumps and downs." % self.name)


class Xiaotiandog (Dog) :
    def game (self) :
        print ("%s fly to the sky to play." % self.name)


class Person (object) :
    def __init__(self,name) -> None:
        self.name = name
    def game_with_dog (self,dog) :
        print ("%s and %s play happily." % (self.name,dog.name))
        dog.game ()

# dog = Dog ("Wang Cai")
dog = Xiaotiandog ("Fly Wang Cai")
person = Person ("Xiao Ming")
person.game_with_dog (dog)
