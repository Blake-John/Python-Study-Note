class Gun :
    def __init__(self,model) -> None:
        self.model = model 
        self.bullet_count = 0
    
    def add_bullet (self,count) :
        # count 参数接受子弹数量
        self.bullet_count += count

    def shoot (self) :
        # 判断子弹数量
        if self.bullet_count <= 0 :
            print ("[%s] has no bullet." % self.model)
            return
        # 发射子弹
        self.bullet_count -= 1
        #提示发射信息
        print ("[%s] tututu…… [%d]" % (self.model,self.bullet_count))

# 定义没有初始值的属性
# 在定义属性时，如果 不知道设置什么初始值，可以设置为 None
# * None 关键字 表示 什么都没有
# *表示一个 空对象，没有方法和属性，是一个特殊的常量
# *可以将 None 赋值给任何一个变量

class Soldier :
    def __init__(self,name) -> None:
        self.name = name
        self.gun = None # 一个对象的 属性，可以是 另一个类创建的对象

    def fire (self) :
        # 判断士兵是否有枪
        if self.gun == None :
            print ("[%s] has no gun……" % self.name)
            return
        # 高喊口号
        print ("[%s] Go go go!" % self.name)
        # 让枪装填子弹
        self.gun.add_bullet (50)
        # 发射子弹
        self.gun.shoot ()

# 创建枪对象
ak47 = Gun ("AK47")
# ak47.add_bullet (50)  
# ak47.shoot ()

#创建士兵对象
zhangsan = Soldier ("Zhang San")
zhangsan.gun = ak47
zhangsan.fire ()
# print (zhangsan.gun)