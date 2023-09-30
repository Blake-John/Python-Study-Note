# *在实际开发中，对象 的 某些属性或方法 可能只希望 在对象的内部被使用，而 不希望在外部被访问到
# *私有属性 就是 对象 不希望公开的 属性
# *私有方法 就是 对象 不希望公开的 方法

# 定义方式
# *在 定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法

class Women :
    def __init__(self,name) -> None:
        self.name = name 
        self.__age = 18
    
    def __secret (self) :
        # 在对象的 方法内部，是可以访问对象的 私有属性
        print ("%s is %d years old." % (self.name,self.__age))

xiaofang = Women ("Xiao Fang")
print (xiaofang) 
# 若 print (xioafang.__age) 则会报错，私有属性不能在外界被直接访问
# 若 xiaofang.__secret () 则会报错，私有方法同样不能在外界被直接访问


# Python 中，并没有 真正意义 的 私有
# *在给 属性、方法 命名时，实际是对 名称 做了一些特殊处理，使得外界无法访问到
# *处理方式：在 名称 前面加上 _类名 => _类名__名称
print (xiaofang._Women__age)
xiaofang._Women__secret ()
