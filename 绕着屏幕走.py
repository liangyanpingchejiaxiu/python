import pygame
import sys
from pygame.locals import *


fullscreen = False
clock =pygame.time.Clock()
pygame.init() #初始化pygame

size =width,height=500,500

screen=pygame.display.set_mode(size,RESIZABLE)# 定义屏幕的大小 可以调整

pygame.display.set_caption("第一次游戏")# 标题

speed =[5,0]# 移动的速度
bg =(255,255,255) #背景颜色 白色

image = pygame.image.load(r"C:\Users\Shinelon\Desktop\5.jpg") #加载图片
position = image.get_rect()

image_right = pygame.transform.rotate(image,90) #旋转90度  rotate 旋转
image_top = pygame.transform.rotate(image,180)
image_left = pygame.transform.rotate(image,270)
image_bottom = image
image = image_top #乌龟如果脚着地 旋转就不对 所以要 上面赋值给下面



r_head =pygame.transform.flip(image,True,False) #头向哪边就定义另一边就行了 flip 是旋转  
l_head =image

while True:# 判断循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type ==KEYDOWN:


        if event.key ==K_F11:
            fullscreen = not fullscreen
            if fullscreen:
                screen =pygame.display.set_mode((1400,1050),FULLSCREEN  | HWSURFACE) # HWSURFACE 硬件加速
                size=width,height=1400,1050
                screen=pygame.display.set_mode(size,RESIZABLE)
                
            else:
                screen=pygame.display.set_mode((500,500),RESIZABLE)
        

        
    position =position.move(speed) #图像移动


    if position.right > width:
        image = image_right   #旋转
        position =image_rect= image.get_rect()
        position.left =width -image_rect.width
        speed = [0,5]

    if position.bottom > height:
        image = image_height
        position =image_rect= image.get_rect()
        position.left =width -image_rect.width
        position.top =height - image_rect,height
        speed = [-5,0]
    if position.left < 0 :
        image = image_left
        position =image_rect= image.get_rect()
        position.left =width -image_rect.width
        position.top =height - image_rect,height
        speed = [0,-5]

    if position.top < 0:
        image = image_top
        position =image_rect= image.get_rect()
        position.left =width -image_rect.width
        position.top =height - image_rect,height
        speed = [5,0]       
                
        
    



    


    screen.fill(bg) #填充颜色

    screen.blit(image,position) #更新图像  # surfce对象就是pygame里面表示的对象  blit flit

    pygame.display.flip() #更新界面 surface更新图像就是把像素修改  移动图像就是帧率 就是FPS 40 刷新40次

    #pygame.time.delay(20)#延迟

    clock.tick(100) #控制帧率
    

