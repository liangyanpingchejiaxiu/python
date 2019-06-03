Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> member=['222','3333','3333333']
>>> member[0]
'222'
>>> member[1]
'3333'
>>> temp=member[0]
>>> member[0]=member[1]
>>> member[1]=temp
>>> member
['3333', '222', '3333333']
>>> member.append('111111')
>>> member
['3333', '222', '3333333', '111111']
>>> member.extend(['123','456'])
>>> member
['3333', '222', '3333333', '111111', '123', '456']
>>> member.insert(0,'梁艳萍’)
		  
SyntaxError: EOL while scanning string literal
>>> member.insert(0,'梁艳萍')
		  
>>> member
		  
['梁艳萍', '3333', '222', '3333333', '111111', '123', '456']
>>> member.remove('123')
		  
>>> member
		  
['梁艳萍', '3333', '222', '3333333', '111111', '456']
>>> del member(1)
		  
SyntaxError: can't delete function call
>>> del member[1]
		  
>>> member
		  
['梁艳萍', '222', '3333333', '111111', '456']
>>> member.pop()
		  
'456'
>>> name=member.pop()
		  
>>> name
		  
'111111'
>>> member.pop(3)
		  
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    member.pop(3)
IndexError: pop index out of range
>>> member
		  
['梁艳萍', '222', '3333333']
>>> member.pop(1)
		  
'222'
>>> list[1]=[123,456]
		  
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list[1]=[123,456]
TypeError: 'type' object does not support item assignment
>>> list1=[123,456]
		  
>>> list2=[456,123]
		  
>>> list1<list2
		  
True
>>> list1+list2
		  
[123, 456, 456, 123]
>>> number=[1,2,3,4,5]
		  
>>> number+member
		  
[1, 2, 3, 4, 5, '梁艳萍', '3333333']
>>> 123 in list1
		  
True
>>> 789 not in list1
		  
True
>>> list4=[1,['梁','按'],3]
		  
>>> 梁 in list4[1]
		  
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    梁 in list4[1]
NameError: name '梁' is not defined
>>> '梁' in  list4[1]
		  
True
>>> list4[1][1]
		  
'按'
>>> list1
		  
[123, 456]
>>> list4
		  
[1, ['梁', '按'], 3]
>>> list4(1:)
		  
SyntaxError: invalid syntax
>>> list4[0:]
		  
[1, ['梁', '按'], 3]
>>> list4[:2]
		  
[1, ['梁', '按']]
>>> list4*=3
		  
>>> lisr4
		  
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    lisr4
NameError: name 'lisr4' is not defined
>>> list4
		  
[1, ['梁', '按'], 3, 1, ['梁', '按'], 3, 1, ['梁', '按'], 3]
>>> list4.count(1)
		  
3
>>> list4.index(3,1,6)
		  
2
>>> list4.reverse
		  
<built-in method reverse of list object at 0x02FDC738>
>>> list4.reverse()
		  
>>> list4
		  
[3, ['梁', '按'], 1, 3, ['梁', '按'], 1, 3, ['梁', '按'], 1]
>>> list4.sort()
		  
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    list4.sort()
TypeError: '<' not supported between instances of 'list' and 'int'
>>> list4.sort(reverse=true)
		  
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    list4.sort(reverse=true)
NameError: name 'true' is not defined
>>> list6=[1,2,3,4,5,3,2,2]
		  
>>> list6*=5
		  
>>> list6
		  
[1, 2, 3, 4, 5, 3, 2, 2, 1, 2, 3, 4, 5, 3, 2, 2, 1, 2, 3, 4, 5, 3, 2, 2, 1, 2, 3, 4, 5, 3, 2, 2, 1, 2, 3, 4, 5, 3, 2, 2]
>>> list6.sort()
		  
>>> list6
		  
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
>>> list6.sort(reverse=true)
		  
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list6.sort(reverse=true)
NameError: name 'true' is not defined
>>> list6.sort(reverse=True)
		  
>>> list6
		  
[5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]
>>> 
		  
>>> list1
		  
[123, 456]
>>> list2
		  
[456, 123]
>>> list1=list2
		  
>>> list1
		  
[456, 123]
>>> list2.append(111)
		  
>>> list2
		  
[456, 123, 111]
>>> list1
		  
[456, 123, 111]
>>> list3
		  
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list3
NameError: name 'list3' is not defined
>>> list9=list2[:]
		  
>>> list9
		  
[456, 123, 111]
>>> list2.remove(111)
		  
>>> list2
		  
[456, 123]
>>> list9
		  
[456, 123, 111]
>>> 
