Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>   def fan(n):
	
SyntaxError: unexpected indent
>>> def fan(n):
	if n<1:
		print("输入有误")

		
>>> def fan(n):
	if n<1:
		print("输入有误")
		return -1
	if n==1 or n==2:
		return 1
	else:
		return fan(n-1)+fan(n-2)

	
>>> result=fan(5)
>>> if result!=-1:
	print("总共有%d对小兔崽子:",%result)
	
SyntaxError: invalid syntax
>>>  if result!=-1:
	print("总共有%d对小兔崽子:"%result)
	
SyntaxError: unexpected indent
>>> if result!=-1:
	print("总共有%d对小兔崽子:"%result)

	
总共有5对小兔崽子:
>>>  def han(n,x,y,z):
	
SyntaxError: unexpected indent
>>> def han(n,x,y,z):
	if n==1:
		print(x,' --> ',z)
	else:
		han(n-1,x,z,y) #将第n-1放在y盘上
		print(x,' --> ',z)#将第n层放在z上
		han(n-1,y,x,z)#再将n-1放在n层上
		#方法就是先把 n-1层放在z再把n层放在y再把n-1层放在n层上

		
>>> n=int(input('请输入汉诺塔的层数'))
请输入汉诺塔的层数5
>>> han(5,x,y,z)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    han(5,x,y,z)
NameError: name 'x' is not defined
>>> han(7,'x','y','z')
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
z  -->  x
y  -->  x
z  -->  y
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
y  -->  x
z  -->  y
z  -->  x
y  -->  x
y  -->  z
x  -->  z
x  -->  y
z  -->  y
x  -->  z
y  -->  x
y  -->  z
x  -->  z
>>> n=int(input('请输入汉诺塔的层数')):
	
SyntaxError: invalid syntax
>>> 
