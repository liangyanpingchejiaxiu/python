Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	f=open('1.txt','wr')
	f.write('helloworld')
	print(f.read())
	f.close()
except ValueError as reason:
	print('文件出错\n错误的原因是:'+str(reason))

	
文件出错
错误的原因是:must have exactly one of create/read/write/append mode
>>> try:
	sum=1+'1'
	f=open('1.txt','wr')
	f.write('helloworld')
	print(f.read())
	f.close()
except ValueError as reason:
	print('文件出错\n错误的原因是:'+str(reason))
except TypeError as reason:
	print('类型出错\n错误的原因是:'+str(reason))

类型出错
错误的原因是:unsupported operand type(s) for +: 'int' and 'str'
>>> try:
	f=open('1.txt','wr')
	f.write('helloworld')
	print(f.read())
	f.close()
except (TypeError,ValueError ):
	print('文件出错:')

文件出错:
>>> raise TypeError('类型出错的异常')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    raise TypeError('类型出错的异常')
TypeError: 类型出错的异常
>>> 
