import pygame
import sys
from pygame.locals import *
import math


clock =pygame.time.Clock()
pygame.init() #初始化pygame

size =width,height=1000,1000

screen=pygame.display.set_mode(size,RESIZABLE)# 定义屏幕的大小 可以调整

pygame.display.set_caption("第一次游戏")# 标题

image = pygame.image.load(r"C:\Users\Shinelon\Desktop\6.png") #加载图片

#rect(Surface,color,Rect,width=0)  矩形 width 是边框多大
#polygon(Surface,color,pointlist,width=0) 第三个是多边形的顶点坐标
#ellipse(Surface,color,Rect,width=0)  椭圆 是在矩形里面画 如果记性是正方形就是椭圆
#arc(Surface,color,Rect,start_angle,stop_angle,width=1)  弧线  要导入math
#line(Surface,color,star_pos,end_pos,width=1)
#lines(Surface,color,cloed,politlist,width=1) 线段 0 不闭合 1  闭合
#aaline(Surface,color,starpos,endpos,blend=1)
#aalines(Surface,color,closed,pointlist,blend=1) 抗锯齿线段 把模糊的更流畅
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
points = [(300,100),(325,75),(350,100),(350,125),(300,125)]
position = size[0]//2,size[1]//2
moving = False

clock = pygame.time.Clock()

while True:# 判断循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button ==1:
                moving = True
        if event.type == MOUSEBUTTONUP:
            if event.button ==1:
                moving = False
    if moving:
        position = pygame.mouse.get_pos() 
                





    screen.fill(white) #填充颜色

    pygame.draw.rect(screen,black,(50,50,150,50),0)
    pygame.draw.rect(screen,white,(200,50,250,100),1)
    pygame.draw.polygon(screen,green,points,1)
    pygame.draw.circle(screen,red,position,25,1) #圆的中心点  半径
    pygame.draw.circle(screen,red,position,50,1) #圆的中心点  半径
    pygame.draw.ellipse(screen,red,(300,50,100,50),1)
    pygame.draw.arc(screen,black,(200,200,400,200),0,math.pi,1) #0 到180度
    pygame.draw.arc(screen,black,(200,500,400,500),0,math.pi,1) # 180到360
    
    

    pygame.display.flip() #更新界面 surface更新图像就是把像素修改  移动图像就是帧率 就是FPS 40 刷新40次

    clock.tick(10)
