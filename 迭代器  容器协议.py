Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Countlist:
	def __init__(self,*args):
		self.values=[x for x in args]
		self.count ={}.fromkeys(range(len(self.values)),0)
	def __len__(self):
		return len(self.values)
	def __getitem__(self,key):
		self.count[key]+=1
		return self.values[key]

	
>>> #容器协议
>>> #迭代器
>>> string='chaoren'
>>> it=iter(string)
>>> next(it)
'c'
>>> next(it)
'h'
>>> #如果打印完了就会报错
>>>  each=next(it)
SyntaxError: unexpected indent
>>> each=next(it)
>>> print(each)
a
>>> #__iter__(self)返回迭代器本身 next 决定迭代规则
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a,self.b,self.a*self.b
		else:
			raise StopIteration

		
>>> diedai=diedaiqi()
>>> diedai
<__main__.diedaiqi object at 0x03B07BF0>
>>> for each in diedai:
	print(each)

	
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print(each)
KeyboardInterrupt
>>> die=diedaiqi(20)
>>> for each in die:
	print(each)

	
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
None
Traceback (most recent call last):
  File "<pyshell#34>", line 2, in <module>
    print(each)
KeyboardInterrupt
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a,self.b,self.a*self.b
		else:
			raise StopIteration
		return self.a

	
>>> d=diedaiqi(20)
>>> for each in d:
	print(each)

	
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    print(each)
KeyboardInterrupt
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a+=5,self.b=self.a+1
		else:
			raise StopIteration
		
SyntaxError: invalid syntax
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a+=5,self.b+=5
		else:
			raise StopIteration
		
SyntaxError: invalid syntax
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a+=5,self.b
		else:
			raise StopIteration
		return self.a

	
>>> a=diedaiqi(20)
>>> for each in a:
	print(each)

	
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    for each in a:
  File "<pyshell#46>", line 10, in __next__
    self.a+=5,self.b
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
>>> class diedaiqi:
	def __init__(self,n=50):
		self.a=1
		self.b=2
		self.n=n
	def __iter__(self):
		return self
	def __next__(self):
		if self.a<self.n:
			self.a=self.a+5,self.b
		else:
			raise StopIteration
		return self.a

	
>>> b=diedaiqi(40)
>>> for each in b:
	print(each)

	
(6, 2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    for each in b:
  File "<pyshell#52>", line 9, in __next__
    if self.a<self.n:
TypeError: '<' not supported between instances of 'tuple' and 'int'
>>> 
