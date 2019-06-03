import pygame
import sys
from pygame.locals import *
import math
from random import *

#spritecollide(sprite,group,dokill,collided = None) 第一个 指定被检测的精灵 第二个是组 第三个是碰撞的精灵是否删除

#pygame.mixer.Sound() 播放音效 play()  stop() fadeout() 淡出音效 set_volume()设置音量 get_volume() 获取音量
#pygame.mixer.music  背景音乐  load()  载入音乐 play()  stop() fadeout() 淡出音效 set_volume()设置音量 get_volume() 获取音量 queue 添加音乐
class Turtle(pygame.sprite.Sprite):  #动画精灵类
    def __init__(self,image,position,speed,bg_size):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = position
        self.speed = speed
        self.width,self.height = bg_size[0],bg_size[1]   #屏幕的大小  背景图片的大小
        #self.radius = self.rect.width / 2 #图片是矩形的 就加半径 不然还有空隙就判定为碰撞



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
class Glass(pygame.sprite.Sprite):
    
    def __init__(self,glass_image,bg_size):
        #初始化动画精灵
        pygame.sprite.Sprite.__init__(self)


        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left,self.glass_rect.top = \
                                                 (bg_size[0] - self.glass_rect.width)//2,bg_size[1] - self.glass_rect.height
        


        
         

                             
                             
            
            
def main():  #主函数赋值
    pygame.init()


    turtle_image=r"C:\Users\Shinelon\Desktop\8.png"
    bg_image =r"C:\Users\Shinelon\Desktop\10.jpg"
    glass_image =r'C:\Users\Shinelon\Desktop\7.png'

    running = True
    #添加魔性的背景音乐
    pygame.mixer.music.load(r'C:\Users\Shinelon\Desktop\bg1.ogg')
    pygame.mixer.music.play()

    #添加音效


    come_sound = pygame.mixer.Sound(r'C:\Users\Shinelon\Desktop\loser.wav')#进入洞里
    collide_sound = pygame.mixer.Sound(r'C:\Users\Shinelon\Desktop\come.wav')#碰撞
    win_sound = pygame.mixer.Sound(r'C:\Users\Shinelon\Desktop\win.wav')#全部进入
    
    #音乐播放完 游戏结束
    gameover = USEREVENT #创建一个事件
    pygame.mixer.music.set_endevent(gameover) #游戏结束时触发的时间

    


    bg_size = width,height=1024,768
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("控制忍者神龟来拯救地球吧!!!!")

    background = pygame.image.load(bg_image).convert() #加载背景图片


    turtles = []
    group = pygame.sprite.Group() #创建碰撞精灵组
   

    for i in range(5): #要导入随机函数
        position = randint(0,width-100),randint(0,height-100) #赋值
        speed = [randint(-10,10),randint(-10,10)] #一个x轴  一个Y轴
        turtle = Turtle(turtle_image,position,speed,bg_size) #创建对象

        while pygame.sprite.spritecollide(turtle,group,False,pygame.sprite.collide_circle):#当碰撞了  卡住了重新生成
            turtle.rect.left,turtle.rect.top =  randint(0,width-100),randint(0,height-100) #避免出错
            
        
        turtles.append(turtle)
        group.add(turtle)

    glass = Glass(glass_image,bg_size) #创建摩擦板    
                
    clock = pygame.time.Clock()    
        
    

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


            elif event.type == gameover:
                come_sound.play()
                #如果还要播放其他音乐
                #pygame.time.delay(2000) .sound.play()
                running = False


        screen.blit(background,(0,0)) #在0,0 绘制背景图片
        screen.blit(glass.glass_image,glass.glass_rect)

        for each in turtles:
            each.move() #在调用小球之前 每个都移动
            screen.blit(each.image,each.rect)#绘制乌龟


        for each in turtles:
            group.remove(each)#先把碰撞组里的都拿出来


            if  pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1] #当两个碰撞就会
                collide_sound.play()


            group.add(each)    
                
            
            

#让内存中的图像显示出来
        pygame.display.flip()
        clock.tick(30)
        




    
if __name__=="__main__":
    main()

        

