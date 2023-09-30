# 在开发中，如果希望在 创建对象的同时，就设置对象的属性，可以对 __init__ 方法进行 改造
# 1. 把希望设置的属性值，定义成 __init__ 方法的参数
# 2. 在方法内部使用 self.attribute = parameter 接收外部传递的参数
# 3. 在创建对象时，使用 class(attribute1, attribute2...) 调用

class Cat :
    def __init__ (self,new_name) :
    # 增加一个参数来设置属性，使代码更加灵活
      print ("这是一个初始化方法")
      # self.name = "Tom"
      self.name = new_name

    def eat (self) :
        print ("%s want to eat fish." % self.name)

tom = Cat ("Tom")
print (tom.name)
tom.eat ()

lazy_cat = Cat ("Lazy Cat")
lazy_cat.eat ()