Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Newint(int):
	def__add__(self,other):
		
SyntaxError: invalid syntax
>>> class Newint(int):
	def __add__(self,other):
		return int.__add__(self,other)
	#可以把self忽略传进来的数代替other
	def __sub__(self,other):
		return int.__sub__(self,other)
	#减法
	def __mul__(self,other):
		return int.__mul__(self,other)
	#乘法
	# __truediv__(self,other) 真除法 返回小数
	# __floordiv__(self,other) 整数除法 返回整数
	#__mod__(self,other) 取余

	
>>> a = Newint(3)
>>> b = Newint(4)
>>> a + b
7
>>> a *b
12
>>> # 反运算 当a没实现 b就实现

