# 事件 event
# *就是游戏启动后，用户针对游戏所做的操作
# *例如：点击关闭按钮，点击鼠标，按下键盘...

# 监听
# *在 游戏循环 中，判断用户 具体的操作
# > 只有 捕获 到用户具体的操作，才能有针对性的做出响应

# 代码实现
# *pygame 中通过 pygame.event.get() 可以获得 用户当前所做动作 的 事件列表
#   *用户可以同一时间做很多事情
# *提示：这段代码非常的固定，几乎所有的 pygame 游戏都 大同小异！

# # 游戏循环
# while True:
#     # 设置屏幕刷新帧率
#     clock.tick(60)
#     # 事件监听
#     for event in pygame.event.get():
#         # 判断用户是否点击了关闭按钮
#         if event.type == pygame.QUIT:
#             print("退出游戏...")
#             pygame.quit()
#             # 直接退出系统
#             exit()

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
    # 调用 update () 更新显示
    pygame.display.update ()

pygame.quit ()