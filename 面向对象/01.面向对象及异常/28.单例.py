# 单例 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例
#  1.定义一个 类属性，初始值是 None，用于记录 单例对象的引用
#  2.重写 __new__ 方法
#  3.如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果
#  4.返回 类属性 中记录的 对象引用

class MusicPlayer (object) :
    # 记录第一个被创建对象的引用
    instance = None
    def __new__ (cls) :
        # 判断类属性是否为 空对象
        if cls.instance is None :
            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super ().__new__ (cls)
        # 返回类属性保存的对象引用
        return cls.instance

player1 = MusicPlayer ()
print (player1)
player2 = MusicPlayer ()
print (player2)