Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	with open('1.txt','wr') as f:
		for each_line in f:
			print(each_line)
except ValueError as reason:
	print('出错了:'+str(reason))

出错了:must have exactly one of create/read/write/append mode
>>> #有了with就不用管finally
