import pygame
from plane_sprites import *

pygame.init ()

# 创建游戏的窗口
screen = pygame.display.set_mode ((480,700))
# 绘制图像
# 加载图像数据
bg = pygame.image.load ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/background.png")
hero = pygame.image.load ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/me1.png")
# blit 绘制图像
screen.blit (bg,(0,0))
screen.blit (hero,(195,295))
# 更新屏幕显示,可在所有绘制工作完成之后，统一调用一次 update () 函数
pygame.display.update ()

# 创建时钟对象
clock = pygame.time.Clock ()

# 定义 hero_rect 记录飞机初始位置
hero_rect = pygame.Rect (195,295,102,126)

# 创建敌机的精灵
enemy = GameSprite ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/enemy1.png")
enemy1 = GameSprite ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/飞机大战/images/enemy1.png",2)
# 创建的敌机精灵组
enemy_group = pygame.sprite.Group (enemy,enemy1)

# 游戏循环 -> 意味着游戏的正式开始
while True :
    # 设置屏幕刷新帧率
    clock.tick (60)

    # 捕获事件
    # event_list = pygame.event.get ()
    # if len (event_list) > 0 :
    #     print (event_list)

    # 事件监听
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            print ("The game is quited......")
            # quit () 卸载所有代码
            pygame.quit ()
            # exit () 直接终止当前正在执行的程序
            exit ()

    # 修改飞机位置
    hero_rect.y -= 10
    # 判断飞机的位置
    if hero_rect.y <= -hero_rect.height :
        hero_rect.y = 700
    # 调用 blit 方法绘制对象
    screen.blit (bg,(0,0)) # 在绘制飞机图像时先绘制背景图片，覆盖原本的图像
    screen.blit (hero,hero_rect)

    # 让精灵组调用两个方法
    enemy_group.update () # update 让组中所有精灵更新位置
    enemy_group.draw (screen) # draw 在 screen 上绘制精灵


    # 调用 update () 更新显示
    pygame.display.update ()

pygame.quit ()