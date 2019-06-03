Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #协同程序可以中断暂停 需要的时候可以从原来的地方重新获取 打开
>>> # 一但函数里面有yield语句 这个函数就是生成器
>>> # yield相当于 return
>>> def Mygen():
	print('生成器被执行')
	yield 1
	yield 2
	yield 3

	
>>> mygen=Mygen()
>>> next(mygen)
生成器被执行
1
>>> next(mygen)
2
>>> next(mygen)
3
>>> string1='12453'
>>> next(string)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    next(string)
NameError: name 'string' is not defined
>>> next(string1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    next(string1)
TypeError: 'str' object is not an iterator
>>> iter(string1)
<str_iterator object at 0x035A7C30>
>>> next(string1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    next(string1)
TypeError: 'str' object is not an iterator
>>> it=iter(string1)
>>> next(it)
'1'
>>> def libs():
	a = 0
	b = 1
	while True:
		a,b = b,a + b
		yield a
		# 迭代器会返回下一个值 1，1，2所以a=0不会返回 相当于t=a+b a=b b=t

		
>>> for each in libs():
	if each >100:
		break
	print(each,end=' ')

	
1 1 2 3 5 8 13 21 34 55 89 
>>> #生成器如果不用for循环就会只打印一个 记住这次的位置 下次从这里开始
>>> a=[i for i in range(10) if not(i%2) and i %3]
>>> a
[2, 4, 8]
>>> b={i:i%2 ==0 for i in range(10)}
>>> b
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
>>> sum(i for i in range(100) if i %2)
2500
>>> 
