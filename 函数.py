Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def myfirsefunction():
	print("这是我创建的第一个函数！")

	
>>> myfirstfunction
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myfirstfunction
NameError: name 'myfirstfunction' is not defined
>>> myfirstfunction()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    myfirstfunction()
NameError: name 'myfirstfunction' is not defined
>>> myfirsefunction()
这是我创建的第一个函数！
>>> 
>>> def mysecondfunction(name):
	print(name+'我爱你')

	
>>> mysecondfunction(车)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    mysecondfunction(车)
NameError: name '车' is not defined
>>> mysecondfunction('车')
车我爱你
>>> def add(num1,num2):
	result=num1+num2
	print(result)

	
>>> add(1,4)
5
>>> add(1,4)//1+4
5
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    add(1,4)//1+4
TypeError: unsupported operand type(s) for //: 'NoneType' and 'int'
>>> def add(num1,num2):
	return=num1+num2
SyntaxError: invalid syntax
>>> def deduce(num1,num2):
	return(num1-num2)

>>> print(deduce(5,1))
4
>>> 
>>> def wendang():
	"这就是一个函数文档！如果我不用DOC函数就不会显示 函数就只会打印print的"
	print("用了print函数 会打印这条信息")

	
>>> wendang._doc_
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    wendang._doc_
AttributeError: 'function' object has no attribute '_doc_'
>>> def wendang1():
	y"这就是一个函数文档！如果我不用DOC函数就不会显示 函数就只会打印print的"
	print("用了print函数 会打印这条信息")
	
SyntaxError: invalid syntax
>>> def wendang1():
	Y"这就是一个函数文档！如果我不用DOC函数就不会显示 函数就只会打印print的"
	print("用了print函数 会打印这条信息")
	
SyntaxError: invalid syntax
>>> def wen(name):
	'函数定义的name是形参'
	print('传递进来的'+name+'才是实参')

	
>>> wen('梁')
传递进来的梁才是实参
>>> wen.__doc__
'函数定义的name是形参'
>>> def liang(name,words):
	print(name+'says'+words)

	
>>> liang(name='梁艳萍',words='牛逼')
梁艳萍says牛逼
>>> def liang(name=1,words=2):
	print(name+'says'+words)

	
>>> liang()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    liang()
  File "<pyshell#44>", line 2, in liang
    print(name+'says'+words)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> def liang(name='sa',words='sasa'):
	print(name+'says'+words)

>>> liang()
sasayssasa
>>> def test(*params):
	print('参数的长度是:',len(params);
	      
SyntaxError: invalid syntax
>>> def test(*params):
	print('参数的长度是:',len(params)
	printf('第二个参数是:',params[1])
	      
SyntaxError: invalid syntax
>>> def test(*params):
	print('参数的长度是:',len(params)
	print('第二个参数是:',params[1])
	      
SyntaxError: invalid syntax
>>> def test(*params):
	print('参数的长度是:',len(params))
	print('第二个参数是:',params[1])

	      
>>> test(1,2,2,2,2,2,3,5,5,5)
	      
参数的长度是: 10
第二个参数是: 2
>>> 
