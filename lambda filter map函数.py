Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def xx(x):
	return x*4+1

>>> xx(3)
13
>>> lambda x:x*4+1
<function <lambda> at 0x0379C6F0>
>>> g=x:x*4+1
SyntaxError: invalid syntax
>>> g=lambda x:x*4+1
>>> g(5)
21
>>> def add(x,y):
	return x+y

>>> add(3,4)
7
>>> lambda x,y:x+y
<function <lambda> at 0x0411D030>
>>> g=lambda x,y:x+y
>>> g(3,4)
7
>>> list(filter(none,[1,0,false,true]))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(filter(none,[1,0,false,true]))
NameError: name 'none' is not defined
>>>  list(filter(None,[1,0,false,true]))
SyntaxError: unexpected indent
>>> list(filter(none,[1,0,false,true]))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list(filter(none,[1,0,false,true]))
NameError: name 'none' is not defined
>>> list(filter(None,[1,0,false,true]))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(filter(None,[1,0,false,true]))
NameError: name 'false' is not defined
>>> list(filter(None,[1,0,False,True]))
[1, True]
>>> def odd(x):
	x%2

	
>>> temp=range(10)
>>> show=filter(odd,temp)
>>> list(show)
[]
>>> def odd(x):
	return x%2

>>> list(show)
[]
>>> show-filter(lambda x:x%2,range(20))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    show-filter(lambda x:x%2,range(20))
TypeError: unsupported operand type(s) for -: 'filter' and 'filter'
>>> show=filter(lambda x:x%2,range(20))
>>> list(show)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> def jiajia(x,y):
	'map函数就是实现里面函数的功能'
	return x+y

>>> list(map(jiajia,[1,2,3],[4,5,6]))
[5, 7, 9]
>>> jiajia_doc_
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    jiajia_doc_
NameError: name 'jiajia_doc_' is not defined
>>> jiajia()_doc_
SyntaxError: invalid syntax
>>> jiajia_document_
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    jiajia_document_
NameError: name 'jiajia_document_' is not defined
>>> 
