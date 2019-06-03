Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while 1:
	g.msgbox('第一个游戏')
	msg='请选择'
	title='选择'
	choices=['猪','鸡','羊']
	choice=g.choicebox(msg,title,choices)
	g.choicebox('你的选择是:'+str(choice),'你的结果')
	msg='你希望重新开始游戏吗'
	title='重新开始'
	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)

		
Traceback (most recent call last):
  File "<pyshell#5>", line 2, in <module>
    g.msgbox('第一个游戏')
NameError: name 'g' is not defined
>>> import sys
>>> import easygui as g
>>> while 1:
	g.msgbox('第一个游戏')
	msg='请选择'
	title='选择'
	choices=['猪','鸡','羊']
	choice=g.choicebox(msg,title,choices)
	g.choicebox('你的选择是:'+str(choice),'你的结果')
	msg='你希望重新开始游戏吗'
	title='重新开始'
	if g.ccbox(msg,title):
		pass
	else:
		sys.exit(0)

'OK'
'Program logic error - no choices were specified.'
>>> 
