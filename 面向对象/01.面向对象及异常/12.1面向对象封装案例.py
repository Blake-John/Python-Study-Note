# 1.封装 是面向对象编程的一大特点
# 2.面向对象编程的 第一步 —— 将 属性 和 方法 封装 到一个抽象的 类 中
# 3.外界 使用 类 创建 对象，然后 让对象调用方法
# 4.对象方法的细节 都被 封装 在 类的内部

class Person :
    def __init__(self,name,weight) -> None:
        # self.attribute = parameter
        self.name = name
        self.weight = weight
    
    def run (self) :
        print ("%s likes running and running is good for physical health." % self.name)
        self.weight -= 0.5
        # > 在 对象的方法内部，是可以 直接访问对象的属性 的！
    def eat (self) :
        print ("%s is a version and he will lose weight after this meal." % self.name)
        self.weight += 1


    def __str__(self) -> str:
        return "%s weights %.2f kilogram." % (self.name,self.weight)

xiaoming = Person ("Xiao Ming",75.0)
xiaoming.run ()
xiaoming.eat ()
print (xiaoming)


