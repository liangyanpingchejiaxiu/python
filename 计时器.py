Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time as t
>>> class mytimer():
	def __init__(self):
		self.unit=['年','月','日','小时','分钟','秒']
		self.prompt='未开始计时'
		self.last=[]
		self.begin = 0
		self.end = 0
	def __str__(self):
		return self.prompt
	def __add__(self,other):
		prompt:'一起运行了'
		result=[]
		for index in range(6):
			result.append(self.last[index]+other.last[index])
			if result[index]:
				prompt+=(str(result[index])+self.unit[index])
				return prompt
	__repr__=__str__
	#开始计时
	def start(self):
		self.begin=t.localtime()
		self.prompt='请先调用stop()计时'
		print("计时开始")
	def stop(self):
		if not self.begin:
			print('请先调用start()计时')
		else:	
		      self.end=t.localtime()
		      self.calu()
		      print('计时结束')
		 #     self就相当是对象
	def calu(self):
		self.last = []
		self.prompt='总共运行了'
		for index in range(6):
			 self.last.append(self.end[index]-self.begin[index])
			 if self.last[index]:
				 self.prompt+=(str(self.last[index])+self.unit[index])
		self.begin=0
		self.end=0

		
>>> t1=mytimer()
>>> t1.start()
计时开始
>>> t1.stop()
计时结束
>>> t1
总共运行了5秒
>>> t2=mytimer()
>>> t2.start()
计时开始
>>> t2.stop()
计时结束
>>> t1+t2
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t1+t2
  File "<pyshell#2>", line 16, in __add__
    prompt+=(str(result[index])+self.unit[index])
UnboundLocalError: local variable 'prompt' referenced before assignment
>>> 
