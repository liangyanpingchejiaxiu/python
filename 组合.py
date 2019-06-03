Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Turtle:
	def __init__(self,x):
		self.num=x

		
>>> 
>>> class Fish:
	def __init__(self,y):
		self.num=y

		
>>> class Pool:
	def __init__(self,x,y):
		self.turtle=Turtle(x)
		self.fish=Fish(y)
	def print(self):
		print('小鱼有%d只，乌龟%d只'%(self.fish.num,self.turtle.num))

		
>>> pool=Pool(4,4)
>>> pool.print()
小鱼有4只，乌龟4只
>>> class Pool:
	def __init__(self,x,y):
		turtle=Turtle(x)
		fish=Fish(y)
	def print(self):
		print('小鱼有%d只，乌龟%d只'%(fish.num,turtle.num))

		
>>> pool=Pool(4,8)
>>> pool.print()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    pool.print()
  File "<pyshell#19>", line 6, in print
    print('小鱼有%d只，乌龟%d只'%(fish.num,turtle.num))
NameError: name 'fish' is not defined
>>> #组合 把不同类放到一个新类
>>> 
