# 身份运算符用于 比较 两个对象的 内存地址 是否一致 —— 是否是对同一个对象的引用
# *在 Python 中针对 None 比较时，建议使用 is 判断
# | 运算符 | 描述                                    | 实例                            |
# | ------ | ---------------------------------------| ------------------------------- |
# | is     | is 是判断两个标识符是不是引用同一个对象   | x is y，类似 id(x) == id(y)     |
# | is not | is not 是判断两个标识符是不是引用不同对象 | x is not y，类似 id(a) != id(b) |

# is 与 == 区别：
# is 用于判断 两个变量 引用对象是否为同一个 
# == 用于判断 引用变量的值 是否相等

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


class Soldier :
    def __init__(self,name) -> None:
        self.name = name
        self.gun = None # 一个对象的 属性，可以是 另一个类创建的对象

    def fire (self) :
        # 判断士兵是否有枪
        if self.gun is None :  # 此处使用 身份运算符 更好
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