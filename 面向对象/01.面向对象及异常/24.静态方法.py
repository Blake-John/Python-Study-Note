# *在开发时，如果需要在 类 中封装一个方法，这个方法：
#   *既 不需要 访问 实例属性 或者调用 实例方法
#   *也 不需要 访问 类属性 或者调用 类方法
# *这个时候，可以把这个方法封装成一个 静态方法

# 语法如下
# @staticmethod
# def 静态方法名():
#     pass

# *静态方法 需要用 修饰器 @staticmethod 来标识，告诉解释器这是一个静态方法
# *通过 类名. 调用 静态方法

class Dog (object) :
    @staticmethod
    def run () : # 静态方法不需要参数 self
        print ("The dog is running.")
    def eat (self) :
        print ("The dog is eating.")

dog = Dog ()
dog.run ()
Dog.run ()