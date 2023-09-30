# > 由 哪一个对象 调用的方法，方法内的 self 就是 哪一个对象的引用

# *在类封装的方法内部，self 就表示 当前调用方法的对象自己
# *调用方法时，程序员不需要传递 self 参数
# *在方法内部
#   *可以通过 self. 访问对象的属性
#   *也可以通过 self. 调用其他的对象方法

class Cat :
    def eat (self) :
        # 哪一个对象调用的方法，self 就是哪一个对象的引用
        print ("%s want to eat fish." % self.name)
    def drink (self) :
        print ("%s want to drink water." % self.name)

#创建猫对象
tom = Cat ()
# 可以使用 .属性名，利用赋值语句
tom.name = "Tom"
#调用对象内的模块
tom.drink ()
tom.eat ()

#再次创建对象
lazy_cat = Cat ()
lazy_cat.name = "Lazy Cat"
lazy_cat.eat ()
lazy_cat.drink ()

print (tom)
print (lazy_cat)