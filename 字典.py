Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1=dict{'鸭子':'呱呱呱','鸡仔':'狗狗狗狗狗','山羊':'咩咩咩'}
SyntaxError: invalid syntax
>>> dict1=dict(鸭子='呱呱呱')
>>> dict1
{'鸭子': '呱呱呱'}
>>> dict1['鸭子']='呱'
>>> dict1
{'鸭子': '呱'}
>>> dict3={'鸭子':'呱呱呱','鸡仔':'狗狗狗狗狗','山羊':'咩咩咩'}
>>> print('鸭子的叫法是：',dict3['鸭子'])
鸭子的叫法是： 呱呱呱
>>> dict3['猪']='哄哄哄'
>>> dict3
{'鸭子': '呱呱呱', '鸡仔': '狗狗狗狗狗', '山羊': '咩咩咩', '猪': '哄哄哄'}
>>> dict1={}
>>> dict1.fromkeys((1,2,3),'number')
{1: 'number', 2: 'number', 3: 'number'}
>>> for eachkey indict1.keys():
	
SyntaxError: invalid syntax
>>> for eachkey in  dict1.keys():
	print(eachkey)

	
>>> 
>>> dict1.fromkeys(range(3),'number')
{0: 'number', 1: 'number', 2: 'number'}
>>> dict1
{}
>>> dict1=dict1.fromkeys(range(3),'number')
>>> for eachkey in  dict1.keys():
	print(eachkey)

	
0
1
2
>>> for eachvalue in  dict1.values():
	print(eachvalue)

	
number
number
number
>>> for eachItem in  dict1.items():
	print(eachitem)

	
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    print(eachitem)
NameError: name 'eachitem' is not defined
>>> for eachitem in  dict1.items():
	print(eachitem)

	
(0, 'number')
(1, 'number')
(2, 'number')
>>> dict1[1]
'number'
>>> print(dict1[1])
number
>>> a={'liang':'niubi'}
>>> b=a{:}
SyntaxError: invalid syntax
>>> b=a[:]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b=a[:]
TypeError: unhashable type: 'slice'
>>> b=a.copy()
>>> b
{'liang': 'niubi'}
>>> b.setdefault{'小白':'狗'}
SyntaxError: invalid syntax
>>> b.setdefault('小白')
>>> b.setdefault('小青','蛇')
'蛇'
>>> b
{'liang': 'niubi', '小白': None, '小青': '蛇'}
>>> a.setdefault('小白','狗')
'狗'
>>> b=update(a)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b=update(a)
NameError: name 'update' is not defined
>>> b.update(a)
>>> b
{'liang': 'niubi', '小白': '狗', '小青': '蛇'}
>>> b.pop()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> b.pop(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b.pop(1)
KeyError: 1
>>> b.popitem()
('小青', '蛇')
>>> b
{'liang': 'niubi', '小白': '狗'}
>>> b.pop('liang')
'niubi'
>>> b
{'小白': '狗'}
>>> 
