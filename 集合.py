Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num={}
>>> 
>>> type(num)
<class 'dict'>
>>> num1={1,2,3,4,5,5}
>>> type(num1)
<class 'set'>
>>> set1=set([1,2,3,4,4,5,6,7,6])
>>> temp=[]
>>> for each in set1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5, 6, 7]
>>> ste1=list(set(set1))
>>> set1
{1, 2, 3, 4, 5, 6, 7}
>>> 
