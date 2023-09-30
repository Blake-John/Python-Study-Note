class MusicPlayer (object) :
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__ (cls) :
        # 判断类属性是否为 空对象
        if cls.instance is None :
            # 调用父类的方法，为第一个对象分配空间
            cls.instance = super ().__new__ (cls)
        # 返回类属性保存的对象引用
        return cls.instance
    
    def __init__(self) -> None:
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag :
            return
        # 如果没有执行过，再执行初始化动作
        print ("Initialization method.")
        # 修改类属性标记
        MusicPlayer.init_flag = True


player1 = MusicPlayer ()
print (player1)
player2 = MusicPlayer ()
print (player2)