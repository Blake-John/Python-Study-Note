# *在 Python 中 属性的获取 存在一个 向上查找机制
# 1.首先在对象内部查找对象属性
# 2.没有找到就会向上寻找类属性

# *因此，要访问类属性有两种方式：
#   1.类名.类属性
#   2.对象.类属性（不推荐）
# 注意:
#  *如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会影响到 类属性的值

class Tool (object) :
    # 使用赋值语句来定义类属性，记录所有工具对象的数量
    count = 0
    def __init__(self,name) -> None:
        self.name = name
        # 让类属性的值增加
        Tool.count += 1 # 注意：访问类属性需要用 类名 作 前缀

tool1 = Tool ("Axe")
tool2 = Tool ("Hammer")
tool3 = Tool ("Bucket")

tool1.count = 9
print (Tool.count)
print (tool1.count)
print (tool2.count)
print (tool3.count)


