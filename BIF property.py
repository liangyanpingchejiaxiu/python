Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class C:
	x=3333
	y=55555
	name='11'

	
>>> class B(C):
	z=12121

	
>>> issubclass(C,B)
False
>>> isinstance(x,C)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    isinstance(x,C)
NameError: name 'x' is not defined
>>> isinstance('name',C)
False
>>> b=B()
>>> c=C()
>>> isinstance(b,B)
True
>>> hasattr(b,'x')
True
>>> getattr(b,'z')
12121
>>> setattr(b,'old','20')
>>> getattr(b,'old')
'20'
>>> delattr(b,'old')
>>> hasattr(b,'old')
False
>>> class Z:
	def __init__(self,size=10):
		self.size=size
	def getsize(self):
		return self.size
	def setsize(self,value):
		sele.size=value
	def delsize(self):
		def self.size
		
SyntaxError: invalid syntax
>>> class Z:
	def __init__(self,size=10):
		self.size=size
	def getsize(self):
		return self.size
	def setsize(self,value):
		sele.size=value
	def delsize(self):
		def self.size
		
SyntaxError: invalid syntax
>>> class Z:
	def __init__(self,size=10):
		self.size=size
	def getsize(self):
		return self.size
	def setsize(self,value):
		sele.size=value
	def delsize(self):
		def self.size
		
SyntaxError: invalid syntax
>>> class Z:
	def __init__(self,size=10):
		self.size=size
	def getsize(self):
		return self.size
	def setsize(self,value):
		sele.size=value
	def delsize(self):
		del self.size
	x=property(getsize,setsize,delsize)

	
>>> z=Z()
>>> z.getsize()
10
>>> z.x()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    z.x()
TypeError: 'int' object is not callable
>>> class Z:
	def __init__(self,size=10):
		self.size=size
	def getsize(self):
		return self.size
	def setsize(self,value):
		sele.size=value
	def delsize(self):
		del self.size
	r=property(getsize,setsize,delsize)

	
>>> z.r()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    z.r()
AttributeError: 'Z' object has no attribute 'r'
>>> z=Z()
>>> z.r
10
>>> z.=15
SyntaxError: invalid syntax
>>> z.r=15
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    z.r=15
  File "<pyshell#39>", line 7, in setsize
    sele.size=value
NameError: name 'sele' is not defined
>>> z.setsize=15
>>> z.size
10
>>> z.r
10
>>> z.r=15
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    z.r=15
  File "<pyshell#39>", line 7, in setsize
    sele.size=value
NameError: name 'sele' is not defined
>>> 
