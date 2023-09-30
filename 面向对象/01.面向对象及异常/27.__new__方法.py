# *使用 类名() 创建对象时，Python的解释器 首先 会 调用 __new__ 方法为对象 分配空间
# *__new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：
#   * 在内存中为对象 分配空间
#   * 返回 对象的引用
# * Python 的解释器获得对象的 引用 后，将引用作为 第一个参数，传递给 __init__ 方法

# > 重写 __new__ 方法 的代码非常固定！
# 语法：
# return super().__new__(cls)

# *否则 Python 的解释器 得不到 分配了空间的 对象引用，就不会调用对象的初始化方法
# *注意：__new__ 是一个静态方法，在调用时需要 主动传递 cls 参数

class MusicPlayer (object) :
    def __new__(cls) :
        # 创建对象时，__new__方法会自动被调用
        print ("Creat objects and allocate space.") # 此时用 print 覆盖了父类方法
        # 为对象分配空间
        instance = super ().__new__ (cls)
        # 返回对象的引用
        return instance

    def __init__ (self) :
        print ("Initialise the player.")


player = MusicPlayer ()
print (player)