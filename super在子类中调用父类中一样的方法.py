Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Animal:
	def __init__(self,name):
		self.name=name
	def greet(self):
		print('i am %s'%self.name)

		
>>> class Dog(Animal):
	def greet(self):
		super().greet()
		print('wangwang')

		
>>> dog=Dog('dog')
>>> dog.greet()
i am dog
wangwang
>>> class Dogancester:
	def eat(self):
		print('我们是狗')

		
>>> class Dog(Animal,Dogancester):
	def greet(self):
		super().greet()
		print('wangwang')
	def eat(self):
		super().eat()
		print('不怕狼')

		
>>> dog=Dog('dog')
>>> dog.greet()
i am dog
wangwang
>>> dog.eat()
我们是狗
不怕狼
>>> 
