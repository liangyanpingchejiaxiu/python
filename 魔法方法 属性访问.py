Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class C:
	
	def __getattr__(self,name):
		print('getattr')
	def __getattribute__(self,name):
		print('getattribute')
		return super().__getattribute__(name)
	def __setattr__(self,name,value):
		print('setattr')
		super().__setattr__(name,value)
	def __delattr__(self,name):
		print('delattr')
		super().__delattr__(name)

		
>>> c=C()
>>> c.x
getattribute
getattr
>>> c.x=5
setattr
>>> del c.x
delattr
>>> c1.name='11'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c1.name='11'
NameError: name 'c1' is not defined
>>> c.name='111'
setattr
>>> #getattr 当用户获取一个不存在的属性的时候 出现的行为
>>> # getattribute 当该类的属性被访问时 出现的行为
>>> # setattr 设置 delattr 删除
