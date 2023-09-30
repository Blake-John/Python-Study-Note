# *类属性 就是针对 类对象 定义的属性
#   *使用 赋值语句 在 class 关键字下方可以定义 类属性
#   *类属性 用于记录 与这个类相关 的特征
# *类方法 就是针对 类对象 定义的方法
#   *在 类方法 内部可以直接访问 类属性 或者调用其他的 类方法

# 语法如下
# @classmethod
# def 类方法名(cls):
#     pass

# *类方法需要用 修饰器 @classmethod 来标识，告诉解释器这是一个类方法
# *类方法的 第一个参数 应该是 cls
#   *由 哪一个类 调用的方法，方法内的 cls 就是 哪一个类的引用
#   *这个参数和 实例方法 的第一个参数是 self 类似
#   *提示 使用其他名称也可以，不过习惯使用 cls

# *通过 类名. 调用 类方法，调用方法时，不需要传递 cls 参数(与self参数相似)
# *在方法内部
#    *可以通过 cls. 访问类的属性
#    *也可以通过 cls. 调用其他的类方法

class Tool (object) :
    # 使用赋值语句来定义类属性，记录所有工具对象的数量
    count = 0
    @classmethod
    def show_tool_count (cls) :
        print ("The number of the tools is %d." % cls.count)
    def __init__(self,name) -> None:
        self.name = name
        # 让类属性的值增加
        Tool.count += 1 # 注意：访问类属性需要用 类名 作 前缀

tool1 = Tool ("Bucket")
tool2 = Tool ("Axe")
tool3 = Tool ("Hammer")

Tool.show_tool_count ()

