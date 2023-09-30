# 精灵 和 精灵组
# *在刚刚完成的案例中，图像加载、位置变化、绘制图像 都需要程序员编写代码分别处理
# *为了简化开发步骤，pygame 提供了两个类
#   * pygame.sprite.Sprite 在游戏开发中，通常把 显示图像的对象 叫做精灵 Sprite
#      *属性: 存储 图像数据 image 和 位置 rect 的 对象
#      *方法: update (*args) 更新精灵 位置  kill () 从所有组中删除
#    注意：pygame.sprite.Sprite 并没有提供 image 和 rect 两个属性
#        * 需要程序员从 pygame.sprite.Sprite 派生子类
#        * 并在 子类 的 初始化方法 中，设置 image 和 rect 属性
#   * pygame.sprite.Group 一个 精灵组 可以包含多个 精灵 对象
#      *方法: 
#         * add (*sprites) 向组中增加精灵
#         * sprites () 返回所有精灵列表
#         * update (*args) 让组中所有精灵调用 update 方法
#         * draw (Surface) 将组中所有精灵的 image，绘制到 Surface 的 rect 位置
#           注意：仍然需要调用 pygame.display.update() 才能在屏幕看到最终结果

# 派生精灵子类
# *如果一个类的 父类 不是 object
# *在重写 初始化方法 时，一定要 先 super() 一下父类的 __init__ 方法
# *保证父类中实现的 __init__ 代码能够被正常执行

import pygame

class GameSprite (pygame.sprite.Sprite) :
    """飞机大战游戏精灵"""
    def __init__ (self,image_name,speed = 1) :
        # 调用父类的初始化方法
        super ().__init__ ()
        # 定义对象的属性
        self.image = pygame.image.load (image_name) 
        # image 的 get_rect() 方法，可以返回 pygame.Rect(x, y, width, height) 的对象
        self.rect = self.image.get_rect ()
        self.speed = speed
    
    def update (self) :
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed