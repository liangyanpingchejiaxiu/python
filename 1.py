import random
secret = random.randint(5,15)
temp=input("输入一个数哦")
guess=int(temp)
while(guess!=secret):
    a=input("哎呀，猜错了再来一次吗\n")
    guess=int(a)
    if guess>secret:
        print("大了哦")
    else:
        if guess<secret:
            print("小了哦")
        else:
            print("猜对了哦")
print("游戏结束")            
            
