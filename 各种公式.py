Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temp=(1,)
>>> isinstance(temp,tuple)
True
>>> team=("梁','艳','萍')
	  
SyntaxError: EOL while scanning string literal
>>> team=('梁','艳','萍')
	  
>>> team=team[:3]+('牛逼')+team[3:]
	  
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    team=team[:3]+('牛逼')+team[3:]
TypeError: can only concatenate tuple (not "str") to tuple
>>>  team1=('梁','艳','萍','可')
	  
SyntaxError: unexpected indent
>>> team2=("梁","艳","萍","可")
	  
>>> team2=team2[:3]+("牛逼",)+team2[3:]
	  
>>> team2
	  
('梁', '艳', '萍', '牛逼', '可')
>>> sre="iloveyou"
	  
>>> sre
	  
'iloveyou'
>>> sre[3:]
	  
'veyou'
>>> sre[:4]
	  
'ilov'
>>> sre.translate(sre.maketrans('可','坏了'))
	  
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sre.translate(sre.maketrans('可','坏了'))
ValueError: the first two maketrans arguments must have equal length
>>> str
	  
<class 'str'>
>>> str=asasasasasa
	  
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    str=asasasasasa
NameError: name 'asasasasasa' is not defined
>>> str1=qwqwqw
	  
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    str1=qwqwqw
NameError: name 'qwqwqw' is not defined
>>> str2='sasasa'
	  
>>> str2.translate(str2.makestrans('a','s')）
		   
SyntaxError: invalid character in identifier
>>> str2.translate(str.makestrans('a','s')）
		   
SyntaxError: invalid character in identifier
>>> str='asasasasas'
		   
>>> str.translate(str.maketrans('a','s'))
		   
'ssssssssss'
>>> str.upper()
		   
'ASASASASAS'
>>> del st
		   
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    del st
NameError: name 'st' is not defined
>>> del  str
		   
>>> 
