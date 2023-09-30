# 初始化方法
# *当使用 类名() 创建对象时，会 自动 执行以下操作：
#   1. 为对象在内存中 分配空间 —— 创建对象
#   2. 为对象的属性 设置初始值 —— 初始化方法(init)
# *这个初始化方法 就是 __init__ 方法，__init__ 是对象的 内置方法
# > __init__ 方法是 专门 用来定义一个类 具有哪些属性的方法！

# *在 __init__ 方法内部使用 self.attribute = initial_value 就可以 定义属性
# *定义属性之后，再使用 Cat 类创建的对象，都会拥有该属性

class Cat :
    def __init__ (self) :
      print ("这是一个初始化方法")
      self.name = "Tom"

    def eat (self) :
        print ("%s want to eat fish." % self.name)

tom = Cat ()
print (tom.name)
tom.eat ()