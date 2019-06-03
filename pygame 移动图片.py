import pygame
import sys
from pygame.locals import *


fullscreen = False
clock =pygame.time.Clock()
pygame.init() #初始化pygame

size =width,height=500,500

screen=pygame.display.set_mode(size,RESIZABLE)# 定义屏幕的大小 可以调整

pygame.display.set_caption("第一次游戏")# 标题

speed =[-2,1]# 移动的速度
bg =(255,255,255) #背景颜色 白色


oimage = pygame.image.load(r"C:\Users\Shinelon\Desktop\5.jpg") #加载图片   .convert_alpha() 透明度 0 - 255 透明到不透明
image=oimage #不要对同一个图像进行多次转换 会损失精度 jpg不支持透明 alpha 就是透明度

oimage_rect = oimage.get_rect()
position =image_rect=oimage_rect #获得图像的位置矩形  position = image.get_rect() 
#设置放大缩小比率
ratio=1.0


r_head =pygame.transform.flip(image,True,False) #头向哪边就定义另一边就行了 flip 是旋转  
l_head =image

while True:# 判断循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type ==KEYDOWN:
        if event.key == K_LEFT:
            image = l_head
            speed = [-1,0]
        if event.key ==K_RIGHT:
            image = r_head
            speed = [1,0]
        if event.key ==K_UP:
            speed = [0,-1]
        if event.key ==K_DOWN:
            speed = [0,1]    


        if event.key ==K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen =pygame.display.set_mode((1400,1050),FULLSCREEN  | HWSURFACE) # HWSURFACE 硬件加速
                size=width,height=1400,1050
                screen=pygame.display.set_mode(size,RESIZABLE)
                
            else:
                screen=pygame.display.set_mode((500,500),RESIZABLE)
        #放大缩小恢复
        if event.key==K_EQUALS or event.key==K_MINUS or event.key ==K_SPACE:
            if event.key ==K_EQUALS and ratio<2:
                ratio+=0.1
            if event.key ==K_MINUS and ratio>0.5:
                ratio-=0.1
            if event.key ==K_SPACE :
                ratio = 1.0

            image = pygame.transform.smoothscale(oimage,(int(oimage_rect.width *ratio),int(oimage_rect.height *ratio)) )
            r_head =pygame.transform.flip(image,True,False) #头向哪边就定义另一边就行了 flip 是旋转  
            l_head =image

    if event.type==VIDEORESIZE:#用户调整窗口尺寸
        size =event.size
        width,height=size
        print(size)
        screen=pygame.display.set_mode(size,RESIZABLE)

        
    position =position.move(speed) #图像移动



    if position.left < 0  or position.right >width:
        image = pygame.transform.flip(image,True,False)#图片 左右 垂直翻转
        speed[0] = -speed[0]
    #翻转图像
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]


    screen.fill(bg) #填充颜色

    screen.blit(image,position) #更新图像  # surfce对象就是pygame里面表示的对象  blit flit

    pygame.display.flip() #更新界面 surface更新图像就是把像素修改  移动图像就是帧率 就是FPS 40 刷新40次

    #pygame.time.delay(20)#延迟

    clock.tick(100) #控制帧率
    
