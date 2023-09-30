class Cat :
    def eat (self) :
        # 哪一个对象调用的方法，self 就是哪一个对象的引用
        print ("%s want to eat fish." % self.name)
    def drink (self) :
        print ("%s want to drink water." % self.name)

tom = Cat ()
# tom.name = "Tom"
tom.drink ()
tom.eat ()
tom.name = "Tom" # 程序无法正常执行

# 在日常开发中，不推荐在 类的外部 给对象增加属性
# 如果在运行时，没有找到 属性，程序会报错
# 对象应该包含有哪些属性，应该 封装在类的内部


lazy_cat = Cat ()
lazy_cat.name = "Lazy Cat"
lazy_cat.eat ()
lazy_cat.drink ()

print (tom)
print (lazy_cat)