import pygame

def main () :
    # 将导入的pygame模块初始化
    pygame.init()
    # 设置窗口
    screen = pygame.display.set_mode ((800,600))
    # 设置标题
    pygame.display.set_caption ('大球吃小球')
    running = True
    # 开始一个事件循环来处理发生的事
    while running :
        # 从消息中获取事件并处理
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                running = False

if __name__ == '__main__' :
    main ()
    
    