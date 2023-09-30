# *pygame专门提供了一个类 pygame.time.Clock 可以非常方便的设置屏幕绘制速度 —— 刷新帧率
# *要使用 时钟对象 需要两步：
#   *1）在 游戏初始化 创建一个 时钟对象
#   *2）在 游戏循环 中让时钟对象调用 tick(帧率) 方法 
# * tick 方法会根据 上次被调用的时间，自动设置 游戏循环 中的延时

import pygame

pygame.init ()

# 创建游戏的窗口
screen = pygame.display.set_mode ((480,700))
# 绘制背景图像
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
i = 0
while True :
    # 设置屏幕刷新帧率
    clock.tick (60)
    print (i)
    i += 1

pygame.quit ()