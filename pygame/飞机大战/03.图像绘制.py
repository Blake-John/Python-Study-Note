# *在游戏中，能够看到的 游戏元素 大多都是 图像
#   *图像文件 初始是保存在磁盘上的，如果需要使用，第一步 就需要 被加载到内存
# *要在屏幕上 看到某一个图像的内容，需要按照三个步骤：
#   1.使用 pygame.image.load(path) 加载图像的数据,要用一个变量接受返回值
#   2.使用 游戏屏幕 对象，调用 object.blit(image,position) 方法 将图像绘制到指定位置
#   3.调用 pygame.display.update() 方法更新整个屏幕的显示
# > 提示：要想在屏幕上看到绘制的结果，就一定要调用 pygame.display.update() 方法

# > 可以在 screen 对象完成 所有 blit 方法之后，
#   统一调用一次 display.update 方法，同样可以在屏幕上 看到最终的绘制结果
# *使用 display.set_mode() 创建的 screen 对象 是一个 内存中的屏幕数据对象
#   *可以理解成是 油画 的 画布
# * screen.blit 方法可以在 画布 上绘制很多 图像
#   *例如：英雄、敌机、子弹...
#   *这些图像 有可能 会彼此 重叠或者覆盖
# * display.update() 会将 画布 的 最终结果 绘制在屏幕上，这样可以 提高屏幕绘制效率，增加游戏的流畅度

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