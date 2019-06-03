Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> count=6
>>> def mydun():
	count=10
	print(count)

	
>>> mydun()
10
>>> count
6
>>> def mydun():
	global count
	count=10
	print(count)

	
>>> mydun()
10
>>> count
10
>>> def fun():
	print('fun正在被调用')
	def fun1():
		print('fun1正在被调用')

		
>>> def fun():
	print('fun正在被调用')
	def fun1():
		print('fun1正在被调用')
	fun1()

	
>>> fun()
fun正在被调用
fun1正在被调用
>>> def funx(x):
	def funy(y):
		return x*y
	return y

>>>  def funx(x):
	def funy(y):
		return x*y
	return funy
SyntaxError: unexpected indent
>>> 
>>> def funx(x):
	def funy(y):
		return x*y
	return funy()

>>> def FUN():
	x=5
	def FUN1():
		nonlocal  x
		x*=x
		return x
	return FUN1()

>>> FUN()
25
>>> ef FUN():
	x=5
	def FUN1():
		global x
		x*=x
		return x
	return FUN1()
SyntaxError: invalid syntax
>>> def FUN():
	x=5
	def FUN1():
		global  x
		x*=x
		return x
	return FUN1()

>>> FUN()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    FUN()
  File "<pyshell#43>", line 7, in FUN
    return FUN1()
  File "<pyshell#43>", line 5, in FUN1
    x*=x
NameError: name 'x' is not defined
>>> 
