# dir 内置函数
# * 在Python中 对象 几乎是无所不在的，
#   我们之前学习的 变量、数据、函数 都是对象
# 在Python中可以使用以下两个方法验证：
#   1.在 标识符 / 数据 后输入一个 .，
#     然后按下 TAB 键，iPython 会提示该对象能够调用的 方法列表
#   2.使用内置函数 dir 传入 标识符 / 数据，可以查看对象内的 所有属性及方法
#   > __方法名__ 格式的方法是Python提供的 内置方法 / 属性

# | 序号 |   方法名   | 类型 | 作用                                    |
# | :--: | :--------: | :--: | ---------------------------------------|
# |  01  | `__new__`  | 方法 | 创建对象 时，会被 自动 调用              |
# |  02  | `__init__` | 方法 | 对象被初始化 时，会被 自动 调用           |
# |  03  | `__del__`  | 方法 | 对象被从内存中销毁 前，会被 自动 调用     |
# |  04  | `__str__`  | 方法 | 返回 对象的描述信息，print 函数输出使用   |

# 在Python中要定义一个只包含方法的类，语法格式如下：
# class 类名:
#     def 方法1(self, 参数列表):
#         pass
#     def 方法2(self, 参数列表):
#         pass
#
# *方法的定义格式和之前学习过的函数 几乎一样
# *区别在于第一个参数必须是 self，大家暂时先记住，稍后介绍 self
# > 注意：类名 的 命名规则 要符合 大驼峰命名法

class Cat :
    def eat (self) :
        print ("Little cat want to eat fish.")
    def drink (self) :
        print ("Little cat want to drink water.")

tom = Cat ()
tom.drink ()
tom.eat ()

print (tom)
addr = id (tom)
print ("%d" % addr)
