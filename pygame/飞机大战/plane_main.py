import pygame
from plane_sprites import *

class PlaneGame (object) :
    """飞机大战主游戏"""
    def __init__(self,screen) -> None:
        print ("Game initialization.")
        pygame.init ()
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode (screen)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock ()
        # 调用私有方法，创建精灵和精灵组
        self.__creat_sprite ()
        # 设置定时器事件
        pygame.time.set_timer (CREAT_ENEMY_EVENT,1000)
        pygame.time.set_timer (HERO_FIRE_EVENT,200)

    def __creat_sprite (self) :
        # 创建背景精灵和精灵组
        bg1 = Background (-1)
        bg2 = Background (-1,True)
        self.back_group = pygame.sprite.Group (bg1,bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group ()
        # 创建英雄的精灵和精灵组
        self.hero = Hero (5)
        self.hero_group = pygame.sprite.Group (self.hero)

    def start_game (self) :
        print ("Game Start.")
        while True :
            # 设置刷新帧率
            self.clock.tick (60)
            # 事件监听
            self.__event_handler ()
            # 碰撞检测
            self.__check_collide ()
            # 更新绘制精灵组
            self.__update_sprites ()
            # 更新显示
            pygame.display.update ()
            pass
    def __event_handler (self) :
        for event in pygame.event.get () :
            # 判断是否退出游戏
            if event.type == pygame.QUIT :
                PlaneGame.__game_over ()
            elif event.type == CREAT_ENEMY_EVENT :
                # print ("Enemy planes flying in and play.")
                # 创建敌机精灵
                enemy = Enemy ()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add (enemy)
            elif event.type == HERO_FIRE_EVENT :
                self.hero.fire ()

            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT :
            #     print ("Right") # 只有抬起后再次按键才有下一次执行
        
        # 使用键盘提供的方法获取键盘按键 - 按键元组
        # keys_pressed = pygame.key.get_pressed ()
        # 判断元组中对应按键索引值
        # if keys_pressed[pygame.K_RIGHT] :
        #     # print ("Right")
        #     self.speed = 2
        # if keys_pressed[pygame.K_LEFT] :
        #     # print ("Left")
        #     self.speed = -2


    def __check_collide (self) :
        # 子弹摧毁敌机
        pygame.sprite.groupcollide (self.hero.bullet_group,self.enemy_group,True,True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide (self.hero,self.enemy_group,True)
        # 判断列表是否有内容
        if len (enemies) > 0 :
            # 让英雄牺牲
            self.hero.kill ()
            # 结束游戏
            PlaneGame.__game_over ()
    def __update_sprites (self) :
        self.back_group.update ()
        self.back_group.draw (self.screen)
        self.enemy_group.update () 
        self.enemy_group.draw (self.screen)
        self.hero.bullet_group.update ()
        self.hero.bullet_group.draw (self.screen)
        self.hero_group.update ()
        self.hero_group.draw (self.screen)
        pass

    @staticmethod
    def __game_over () :
        print ("Game over......")
        pygame.quit ()
        exit ()


if __name__ == "__main__" :
    # 创建游戏对象
    game = PlaneGame (SCREEN_RECT.size)
    # 启动游戏
    game.start_game ()