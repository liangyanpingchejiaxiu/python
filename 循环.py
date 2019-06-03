Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> membe=['liang',  'yan',  'ping']
>>> for i  in   membe:
	print(i,len(i))

	
liang 5
yan 3
ping 4
>>> abc="bcd"
>>> for i in abc:
	print(i,end=" ")

	
b c d 
>>> range(5)
range(0, 5)
>>> range(1,6)
range(1, 6)
>>> for i in range(1,20,5):
	print(i,end=' ')

	
1 6 11 16 
>>> a='梁艳平真帅'
>>> answeer=input('请输入一句话')
请输入一句话
>>> while true:
	if answeer==a:
		break
	answer=input('输入错了，再来一次不然不退出哦')
print('恭喜你，猜对了哦')
SyntaxError: invalid syntax
>>> a='梁艳平真帅'
>>> answeer=input('请输入一句话')while true:
	if answeer==a:
		break
	answer=input('输入错了，再来一次不然不退出哦')
print('恭喜你，猜对了哦')

SyntaxError: multiple statements found while compiling a single statement
>>> 
