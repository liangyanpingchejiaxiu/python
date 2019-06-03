 #加载图片   .convert_alpha() 透明度 0 - 255 透明到不透明 jpg不支持透明 alpha 就是透明度(把背景变透明)
# image.set_colorkey((255,255,255))  指定一种背景颜色变透明
# image.set_alpha(200)
# image.get_at(position,center)   获得单个像素的颜色   用image.set_at 改变像素的颜色


import pygame
import sys
from pygame.locals import *


clock =pygame.time.Clock()
pygame.init() #初始化pygame

size =width,height=1000,1000

screen=pygame.display.set_mode(size,RESIZABLE)# 定义屏幕的大小 可以调整

pygame.display.set_caption("第一次游戏")# 标题
bg =(0,0,0)
image = pygame.image.load(r"C:\Users\Shinelon\Desktop\6.png") #加载图片
position =image.get_rect() #获得图像的位置矩形
position.center = width//2,height//2

def blit_alpha(target,source,location,opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(),source.get_height())).convert()
    temp.blit(target,(-x,-y))
    temp.blit(source<(0,0))
    temp.set_alpha(opacity)
    target.blit(temp,location)

    
    
            
        




while True:# 判断循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





    screen.fill(bg) #填充颜色

    screen.blit(image,position) #更新图像  # surfce对象就是pygame里面表示的对象  blit flit

    pygame.display.flip() #更新界面 surface更新图像就是把像素修改  移动图像就是帧率 就是FPS 40 刷新40次

    #pygame.time.delay(20)#延迟

    clock.tick(100) #控制帧率
    
