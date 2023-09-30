import pygame
import sys

pygame.init ()   #初始化模块
size=width,height=1200,600  #a=b,c=10,100
speed=[-2,1]  #设置速度列表
bg=(255,255,255)   #RGB色块 红/绿/蓝
screen=pygame.display.set_mode (size)   #设置屏幕大小
pygame.display.set_caption ("fuck you")  #设置标题
turtle=pygame.image.load ("turtle.png")   #绝对路径，相对路径
position=turtle.get_rect ()  #找到图形矩形框

while True :
    for event in pygame.event.get () :     
        if event.type==pygame.QUIT :  #事件停止
            sys.exit ()  #程序停止
    position=position.move (speed)  #使小乌龟移动
    if position.left<0 or position.right>width :  
        turtle=pygame.transform.flip (turtle,True,False)
        speed [0]=-speed [0]
    if position.top<0 or position.bottom>height :
        speed [1]=-speed [1]
    screen.fill (bg)
    screen.blit (turtle,position)
    pygame.display.flip ()
    pygame.time.delay (10)