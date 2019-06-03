Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "(a) is (b) (c)".format(a="谢",b="sb",c="a")
'(a) is (b) (c)'
>>> "{a} is {b} {c}".format(a="谢",b="sb",c="a")
'谢 is sb a'
>>> "{2} is {0} {1}".format(a="谢",b="sb",c="a")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    "{2} is {0} {1}".format(a="谢",b="sb",c="a")
IndexError: tuple index out of range
>>> "{2} is {0} {1}".format("谢","sb","a")
'a is 谢 sb'
>>> print("\taaa")
	aaa
>>> print("\tt")
	t
>>> print("\[]")
\[]
>>> '{0.1f}{1}'.format(28.666,'gb')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    '{0.1f}{1}'.format(28.666,'gb')
AttributeError: 'float' object has no attribute '1f'
>>> '{0:1f}{1}'.format(28.666,'gb')
'28.666000gb'
>>> '%c' %97
'a'
>>> '%c %c %c' %(97,98)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    '%c %c %c' %(97,98)
TypeError: not enough arguments for format string
>>> '%c %c %c' %(97,98,99)
'a b c'
>>> '%s' % '格式化字符串'
'格式化字符串'
>>> '%d +%d = %d' %(5,7,5+7)
'5 +7 = 12'
>>> 
