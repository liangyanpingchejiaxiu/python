Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #对象=属性加方法 属性为静态 方法为动态
>>> class Turtle:#
	#属性
	color='green'
	weight=10
	legs=4

	
>>> class Turtle:#
	#属性
	color='green'
	weight=10
	legs=4
	#方法
	def climb(self):
		print('我在努力的爬了')

		
>>> tt=Turtle()
>>> tt.climb()
我在努力的爬了
>>> #面向对象又称为oo
>>>  #面向对象的特征 封装 继承：子类自动共享父类之间数据和方法的机制 多态 ：
>>> #class mylist(list):  mylist 继承list的方法和属性  开头字母要大写
>>> class A:
	def fun(self):
		print('i am a')

		
>>> class B:
	def fun(self):
		print('i am b')

		
>>> a=A()
>>> b=B()
>>> a.fun()
i am a
>>> b.fun()
i am b
>>> #虽然方法名相同 但是表达出来的就不同 这就是多态 每种生物都有嘴 但是形状不一样
>>> #方法中的self相当于指针 指向哪里
>>> class Ball:
	def name(self,name):
		self.name=name
		#就相当于self不存在传进去的数就直接代替name但是self一定要写
	def kick(self):
		print('我叫%s,该死的谁踢我'% self.name)

		
>>> a=Ball()
>>> b=Ball()
>>> a.name('1')
>>> b.name('2)
	   
SyntaxError: EOL while scanning string literal
>>> b.name('2')
	   
>>> b=Ball()
	   
>>> #_init_(self)方法 只要实例化一个对象 该方法就会自动被调用
	   
>>> class Ball:
	def _init_(self,name):
		self.name=name
		#就相当于self不存在传进去的数就直接代替name但是self一定要写
	def kick(self):
		print('我叫%s,该死的谁踢我'% self.name)

	   
>>> b=Ball()
	   
>>> b.
	   
SyntaxError: invalid syntax
>>> b,kick('1')
	   
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b,kick('1')
NameError: name 'kick' is not defined
>>> class person:
	   name='梁'
	   __name1='艳'#前面加__两根下划线表示私有
	   def getname(self):
	   return self.__name1
	   
SyntaxError: expected an indented block
>>> class person:
	   name='梁'
	   __name1='艳'#前面加__两根下划线表示私有
	   def getname(self):
	           return  self.__name1

	   
>>> p=person()
	   
>>> p.name
	   
'梁'
>>> p.__name1
	   
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    p.__name1
AttributeError: 'person' object has no attribute '__name1'
>>> #私有的 会报错所以就要用方法调用
	   
>>> p.getname()
	   
'艳'
>>> 
