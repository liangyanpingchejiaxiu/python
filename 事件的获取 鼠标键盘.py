import pygame
import sys



pygame.init() #初始化pygame

size = width,height=500,500
screen = pygame.display.set_mode(size)

pygame.display.set_caption("第二次游戏")# 标题

bg = (0,0,0)

font = pygame.font.Font(None,20) #字体 默认为电脑的
line_height = font.get_linesize() #知道行高 不能大于 height
position = 0
screen.fill(bg) #填充屏幕 黑色



while True:# 判断循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            


        screen.blit(font,render(str(event),True,(0,255,0)),(0,position))
                         #消除锯齿  绿色 从0开始 到position
        position = line_height #把 行高赋值给position
        
        if position > height:
            position = 0
            screen.fill(bg)

    pygame.display.flip()        
    


   

    
    

