Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Nint(int):
	def __radd__(self,other):
		return int.__sub__(self,other)
	#反运算 当第一个值没有实现运算 就由第二个来 第一个为 a 第二个为b 都是函数的对象 那么就不会进行反运算 如果第一个不是 函数的对象就进行反运算

	
>>> a =Nint(5)
>>> b=Nint(5)
>>> a+b
10
>>> #都是函数对象 所以正常
>>> 1+b
4
>>> c=3
>>> c+b
2
>>> #1和c不是函数对象所以反运算
>>> 
