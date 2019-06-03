import pygame
import sys
from pygame.locals import *
import math
from random import *



class Turtle(pygame.sprite.Sprite):  #动画精灵类
    def __init__(self,image,position,speed,bg_size):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]   #屏幕的大小  背景图片的大小



    def move(self):
        self.rect = self.rect.move(self.speed)


        if self.rect.right < 0:
            self.rect.left = self.width #小球在右边出去之后 左边出来 上面出去 下面出来
        elif self.rect.left > self.width:# 球的最上端出去 最下端出来 # right 相当于 width
            self.rect.right = 0

        elif self.rect.bottom < 0 :
            self.rect.top = self.height

        elif self.rect.top > self.height:
            self.rect.bottom = 0


def collide_check(item,target):
    collide_turtles = []
    for each in target: #取出每个球 圆心距 根号 (x1-x2)平方＋（y1-y2)平方
        
        distance = math.sqrt(math.pow((item.rect.center[0] - each.rect.center[0]),2) +
                           math.pow((item.rect.center[1] - each.rect.center[1]),2))
        #是否碰撞就是检测圆心距跟半径的关系  大于 不碰撞  等于小于碰撞
        if distance <=(item.rect.width + each.rect.width)/2:
            collide_turtles.append(each)

    return collide_turtles        
                             
                             
            
            
def main():  #主函数赋值
    pygame.init()


    turtle_image=r"C:\Users\Shinelon\Desktop\8.png"
    bg_image =r"C:\Users\Shinelon\Desktop\10.jpg"


    running = True


    bg_size = width,height=1024,768
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("控制忍者神龟来拯救地球吧!!!!")

    background = pygame.image.load(bg_image).convert() #加载背景图片


    turtles = []
    turtle_num = 5

    for i in range(turtle_num): #要导入随机函数
        position = randint(0,width-100),randint(0,height-100) #赋值
        speed = [randint(-10,10),randint(-10,10)] #一个x轴  一个Y轴
        turtle = Turtle(turtle_image,position,speed,bg_size) #创建对象
        while collide_check(turtle,turtles):
            turtle.rect.left,turtle.rect.top = randint(0,width-100),randint(0,height-100) #在出现之前调用 防止出错
            
        turtles.append(turtle)
    clock = pygame.time.Clock()    
        
    

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


        screen.blit(background,(0,0)) #在0,0 绘制背景图片

        for each in turtles:
            each.move() #在调用小球之前 每个都移动
            screen.blit(each.image,each.rect)#绘制乌龟


        for i in range(turtle_num):
            item = turtles.pop(i) # 自己不能跟自己碰撞 所以要把自己拿出来


            if collide_check(item,turtles):
                item.speed[0] = -item.speed[0]
                item.speed[1] = -item.speed[1]

            turtles.insert(i,item)  #再把拿出来的一个放进去    
            

#让内存中的图像显示出来
        pygame.display.flip()
        clock.tick(30)
        




    
if __name__=="__main__":
    main()

        
