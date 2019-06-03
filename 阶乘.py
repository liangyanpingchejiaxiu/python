Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def digui(x):
	if x==1:
		return 1
	else:
		return x * digui(x-1)

	
>>> print(digui(5))
120
>>> def function(x):
	result=x
	for i in range(1,x):
		result*=i
	return result

>>> function(58)
2350561331282878571829474910515074683828862318181142924420699914240000000000000
>>> 
