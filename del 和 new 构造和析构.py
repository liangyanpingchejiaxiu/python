Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Capstr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)
	# 只有不可变的类 才用new来改变

	
>>> a = Capstr('i love you')class Capstr(str):
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)
	# 只有不可变的类 才用new来改变
	
SyntaxError: invalid syntax
>>> a= Capstr('i love you')
>>> a
'I LOVE YOU'
>>> class C:
	def __init__(self):
		print('diaoyong')
	def __del__(self):
		print('当所有标签都被删除时，我会被调用')

		
>>> c1=C()
diaoyong
>>> c2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c2
NameError: name 'c2' is not defined
>>> c2=c1
>>> c3=c2
>>> del c3
>>> del c2
>>> del c1
当所有标签都被删除时，我会被调用
>>> 
