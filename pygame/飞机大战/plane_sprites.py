import random
import pygame


# 常量 的 命名 应该 所有字母都使用大写，单词与单词之间使用下划线连接
# 提示：Python 中并没有真正意义的常量，只是通过命名的约定,所有字母都是大写的就是常量，开发时不要轻易的修改！
SCREEN_RECT = pygame.Rect (0,0,480,700) # 屏幕大小
FRAME_PER_SEC = 60 # 帧率
CREAT_ENEMY_EVENT = pygame.USEREVENT # 敌机的定时器事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1 # 英雄发射子弹事件

class GameSprite (pygame.sprite.Sprite) :
    """飞机大战游戏精灵"""
    def __init__ (self,image_name,speed) :
        # 调用父类的初始化方法
        super ().__init__ ()
        # 定义对象的属性
        self.image = pygame.image.load (image_name) 
        # image 的 get_rect() 方法，可以返回 pygame.Rect(x, y, width, height) 的对象
        self.rect = self.image.get_rect ()
        self.speed = speed
    
    def update (self) :
        # 在屏幕的垂直方向上移动
        self.rect.y -= self.speed


class Background (GameSprite) :
    """游戏背景精灵"""
    def __init__ (self,speed,is_alt = False) :
        super ().__init__ ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/background.png",speed) 
        # 判断是否为交替图像
        if is_alt :
            self.rect.y = self.rect.height
    def update (self) :
        # 调用父类的方法实现
        super ().update ()
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height :
            self.rect.y = -self.rect.height


class Enemy (GameSprite) :
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵
        super().__init__("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/enemy1.png",0)
        # 指定敌机的初始随机速度
        self.speed = random.randint (-3,-1)
        # 指定敌机的初始随机位置
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint (0,max_x)
        # self.rect.y = -self.rect.height
        self.rect.bottom = 0
    def update (self) :
        # 调用父类方法，保持垂直方向上的飞行
        super ().update ()
        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height :
            # print ("Kill the enemy.")
            # pygame.sprite.Sprite.kill (self)
            self.kill ()
    def __del__ (self) :
        # print ("The enemy is die on %s" % self.rect)
        pass


class Hero (GameSprite) :
    """英雄精灵"""
    def __init__(self,speed):
        super().__init__("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/me1.png",speed)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的精灵组
        self.bullet_group = pygame.sprite.Group ()
    def update (self) :
        key_pressed = pygame.key.get_pressed ()
        if key_pressed[pygame.K_RIGHT] :
            self.rect.x += self.speed 
        if key_pressed[pygame.K_LEFT] :
            self.rect.x -= self.speed 
        if key_pressed[pygame.K_UP] :
            self.rect.y -= self.speed 
        if key_pressed[pygame.K_DOWN] :
            self.rect.y += self.speed                    # 两种方法，一种设置位置
        if self.rect.x <= 0 :                            # 一种设置反向移动
            self.rect.x += self.speed
        if self.rect.right >= SCREEN_RECT.right :
            self.rect.right = SCREEN_RECT.right
        if self.rect.y <= 0 :
            self.rect.y += self.speed
        if self.rect.bottom >= SCREEN_RECT.bottom :
            self.rect.bottom = SCREEN_RECT.bottom
    
    def fire (self) :
        # print ("Fire!!!")
        for i in (0,1,2) :
            # 创建子弹精灵
            bullet = Bullet (7)
            # 设置子弹初始位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 将精灵添加到精灵组
            self.bullet_group.add (bullet)


class Bullet (GameSprite) :
    def __init__(self,speed):
        super().__init__("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/bullet1.png", speed)
    def update (self) :
        # 调用父类方法，让子弹沿垂直方向飞行
        super ().update ()
        if self.rect.bottom <= 0 :
            self.kill ()
        
    # def __del__ (self) :
    #     print ("Bullet is destroyed.")