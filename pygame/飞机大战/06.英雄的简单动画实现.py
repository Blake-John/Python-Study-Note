# 1.在 游戏初始化 定义一个 pygame.Rect 的变量记录英雄的初始位置
# 2.在 游戏循环 中每次让 英雄 的 y - 1 —— 向上移动 
# 3. y <= 0 将英雄移动到屏幕的底部
# > 提示：
# > *每一次调用 update() 方法之前，需要把 所有的游戏图像都重新绘制一遍
# > *而且应该 最先 重新绘制 背景图像

import pygame

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

while True :
    # 设置屏幕刷新帧率
    clock.tick (60)
    
    # 修改飞机位置
    hero_rect.y -= 10
    # 判断飞机的位置
    if hero_rect.y <= -hero_rect.height :
        hero_rect.y = 700
    # 调用 blit 方法绘制对象
    screen.blit (bg,(0,0)) # 在绘制飞机图像时先绘制背景图片，覆盖原本的图像
    screen.blit (hero,hero_rect)
    # 调用 update () 更新显示
    pygame.display.update ()

pygame.quit ()