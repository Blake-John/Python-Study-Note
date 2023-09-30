# | 序号 |  方法名   | 类型 | 作用                                |
# | :--: | :-------: | :--: | -----------------------------------|
# |  01  | __del__ | 方法 | 对象被从内存中销毁 前，会被 自动 调用   |
# |  02  | __str__ | 方法 | 返回 对象的描述信息，print 函数输出使用 |

# *当使用 类名() 创建对象时，为对象 分配完空间 后，自动 调用 __init__ 方法
# *当一个 对象被从内存中销毁 前，会 自动 调用 __del__ 方法

# 生命周期
# *一个对象从调用 类名() 创建，生命周期开始
# *一个对象的 __del__ 方法一旦被调用，生命周期结束
# *在对象的生命周期内，可以访问对象属性，或者让对象调用方法

class Cat :
    def __init__ (self,new_name) :
        self.name = new_name
        print ("%s is coming." % self.name)
    def __del__ (self) :
        print ("%s is going away." % self.name)

# tom 是一个全局变量
tom = Cat ("Tom")
print (tom.name)

# del 关键字可以删除一个对象
del tom
print ("-" * 50)