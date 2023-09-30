# 游戏中的动画实现原理
# *跟 电影 的原理类似，游戏中的动画效果，本质上是 快速 的在屏幕上绘制 图像
#   *电影是将多张 静止的电影胶片 连续、快速的播放，产生连贯的视觉效果！
# *一般在电脑上 每秒绘制 60 次，就能够达到非常 连续 高品质 的动画效果
#   *每次绘制的结果被称为 帧 Frame

# 游戏的两个组成部分
# > 游戏循环的开始 就意味着 游戏的正式开始
# 1.游戏的初始化
#  *设置游戏窗口
#  *绘制图像初始位置
#  *设置游戏时钟
# 2.游戏循环
#  *设置刷新帧率
#  *检测用户交互
#  *更新所有图像位置
#  *更新屏幕显示

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
while True :
    pass

pygame.quit ()