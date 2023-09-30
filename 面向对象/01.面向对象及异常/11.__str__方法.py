# *在 Python 中，使用 print 输出 对象变量，默认情况下，
#  会输出这个变量 引用的对象 是 由哪一个类创建的对象，以及 在内存中的地址（十六进制表示）
# *如果在开发中，希望使用 print 输出 对象变量 时，能够打印 自定义的内容，就可以利用 __str__ 这个内置方法了
# > 注意： __str__ 方法必须返回一个 字符串

class Cat :
    def __init__ (self,new_name) :
        self.name = new_name
        print ("%s is coming." % self.name)
    def __del__ (self) :
        print ("%s is going away." % self.name)
    def __str__(self) :
        # 必须返回一个字符串
        return "I'm a cat named %s." % self.name

# tom 是一个全局变量
tom = Cat ("Tom")
print (tom)