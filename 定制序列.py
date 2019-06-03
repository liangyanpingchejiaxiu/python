Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Count:
	deef __init__(self,*args):
		
SyntaxError: invalid syntax
>>> class Count:
	def __init__(self,*args):
		self.vales = [x for x in args]
		self.count = {}.formkeys(range(len(self.values)),0)

		
>>> class Count:
	def __init__(self,*args):
		self.vales = [x for x in args]
		self.count = {}.formkeys(range(len(self.values)),0)
	def __len__(self):
		return len(self.values)
	def __getitem__(self,key):
		self.count[key] += 1
		return self.values[key]

	
>>> c1=Count[1,3,5,7,9]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c1=Count[1,3,5,7,9]
TypeError: 'type' object is not subscriptable
>>> #key表示的是列表的下标 
