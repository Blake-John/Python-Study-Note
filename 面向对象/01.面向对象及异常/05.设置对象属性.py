# 给对象增加属性
# *在Python中，要 给对象设置属性，非常的容易，但是 不推荐使用
#   *因为：对象属性的封装应该封装在类的 内部
# *只需要在 类的外部的代码 中直接通过 . 设置一个属性即可
# 如： object.attribute = ""
# > 注意：这种方式虽然简单，但是不推荐使用！

class Cat :
    def eat (self) :
        print ("Little cat want to eat fish.")
    def drink (self) :
        print ("Little cat want to drink water.")

#创建猫对象
tom = Cat ()
# 可以使用 . 属性名，利用赋值语句
tom.name = "Tom"
#调用对象内的模块
tom.drink ()
tom.eat ()

#再次创建对象
lazy_cat = Cat ()
tom.name = "大懒猫"
lazy_cat.eat ()
lazy_cat.drink ()

print (tom)
print (lazy_cat)