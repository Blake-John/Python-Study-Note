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
# 同一个类 创建的 多个对象 之间，属性 互不干扰
xiaomei = Person ("Xiao Mei",45.0)
xiaomei.eat ()
xiaomei.run ()
print (xiaomei)