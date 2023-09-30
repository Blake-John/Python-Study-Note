class Cat :
    def eat (self) :
        print ("Little cat want to eat fish.")
    def drink (self) :
        print ("Little cat want to drink water.")

#创建猫对象
tom = Cat ()
#调用对象内的模块
tom.drink ()
tom.eat ()

#再次创建对象
lazy_cat = Cat ()

lazy_cat.eat ()
lazy_cat.drink ()

print (tom)
print (lazy_cat)