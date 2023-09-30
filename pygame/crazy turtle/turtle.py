import pygame as py
import sys
from pygame.locals import *  #将pygame的所有常量名导入

py.init ()
size=width,height=600,400
bg=(255,255,255)
speed=[0,0]
clock=py.time.Clock ()
screen=py.display.set_mode (size,RESIZABLE)  #设置可调节窗口尺寸的前提
py.display.set_caption ("初次见面，请多指教")
fullscreen=False
ratio=1.0  #设置放大缩小比例
oturtle=py.image.load ("C:/Users/Blake John/OneDrive/桌面/学习/程序/pygame/crazy turtle/turtle.png")
oturtle_rect=oturtle.get_rect ()
turtle=oturtle
position=turtle_rect=oturtle_rect
l_head=turtle  #乌龟朝左
r_head=py.transform.flip (turtle,True,False)  #乌龟朝右
u_head=turtle  #乌龟朝上
d_head=py.transform.flip (turtle,False,True)  #乌龟朝下



while True :
    for event in py.event.get () :
        if event.type == QUIT :
            sys.exit ()
        if event.type == KEYDOWN :
            #放大、缩小乌龟（=、-），空格恢复原始尺寸
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE :
                #设置最大只能放大一倍，缩小一半
                if event.key == K_EQUALS and ratio < 2 :
                    ratio+=0.1
                if event.key == K_MINUS and ratio > 0.5 :
                    ratio-=0.1
                if event.key == K_SPACE :
                    ratio=1
                turtle=py.transform.smoothscale (oturtle,(int (oturtle_rect.width*ratio),int (oturtle_rect.height*ratio)))
                #修改乌龟两个朝向的Surface对象，否则一单击移动便打回原形
                l_head=turtle
                r_head=py.transform.flip (turtle,True,False)
                u_head=turtle
                d_head=py.transform.flip (turtle,False,True)
                #获得小乌龟缩放后的新尺寸
                turtle_rect=turtle.get_rect ()
            position.width,position.height=turtle_rect.width,turtle_rect.height
            if event.key == K_F11 :  #全屏设置
                fullscreen=not fullscreen  
                if fullscreen :
                    screen=py.display.set_mode ((1920,1080),FULLSCREEN | HWSURFACE)
                else :
                    screen=py.display.set_mode (size)
            if event.type == VIDEORESIZE :
                size=event.size
                width,height=size
                print (size)
                screen=py.display.set_mode (size,RESIZABLE)
            if event.key == K_LEFT :  #向左
                speed=[-10,0]
                turtle=l_head
            if event.key ==K_RIGHT :  #向右
                speed=[10,0]
                turtle=r_head
            if event.key == K_UP :  #向上
                speed=[0,-10]
                turtle=u_head
            if event.key == K_DOWN :  #向下
                speed=[0,10]
                turtle=d_head
    position=position.move (speed)
    if position.left < 0 :  #超出舞台左时改方向
        speed [0]=-speed [0]
        turtle=r_head
    if position.right > width :  #超出舞台右时改方向
        speed [0]=-speed [0]
        turtle=l_head
    if position.top < 0 :  #超出舞台上时改方向
        speed [1]=-speed [1]
        turtle=d_head
    if position.bottom > height :  #超出舞台下时改方向
        speed [1]=-speed [1]
        turtle=u_head
    screen.fill (bg)
    screen.blit (turtle,position)
    py.display.flip ()
    clock.tick (30)

