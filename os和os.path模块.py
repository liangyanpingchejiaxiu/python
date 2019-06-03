Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.listdir('E:\\')
['$RECYCLE.BIN', '26', 'DownLoadRecord.ini', 'LOL_V4.0.1.9_LCU_FULL.7z.001', 'LOL_V4.0.1.9_LCU_FULL.7z.002', 'LOL_V4.0.1.9_LCU_FULL.7z.003', 'LOL_V4.0.1.9_LCU_FULL.exe', 'Program Files', 'sanguozhanji3', 'sethotkey.log', 'SOFT_REPAIR', 'System Volume Information', 'Warcraft3_1.24E', '英雄联盟', '英雄联盟LCU']
>>> os.mkdir('E:\\1')
>>> os.makedirs('E:\\2\\3')
>>> os.remove('E:\\1\\1.txt.txt')
>>> os.rmdir('E:\\1')
>>> os.removedirs('E:\\2\\3'0
		  
SyntaxError: invalid syntax
>>> os.removedirs('E:\\2\\3')
		  
>>> os.rename('E:\\26','E:\\1')
		  
>>> os.system('cmd')
		  
-1073741510
>>> os.system('calc')
		  
0
>>> os.curdir
		  
'.'
>>> os.listdir(.)
		  
SyntaxError: invalid syntax
>>> os.listdir('.)
	       
SyntaxError: EOL while scanning string literal
>>> os.listdir('.')
	       
['1.txt', 'C#', 'DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'linux', 'NEWS.txt', 'python', 'python.exe', 'python3.dll', 'python37.dll', 'pythonw.exe', 'Scripts', 'tcl', 'Tools', 'vcruntime140.dll', 'Visio2010', '作业', '学生选课系统', '操作系统', '软件工程', '魔鬼作坊']
>>> os.getpwd()
	       
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    os.getpwd()
AttributeError: module 'os' has no attribute 'getpwd'
>>> os.getcwd()
	       
'F:\\桌面文件'
>>> os.path.splitext('E:\\1\\b\\aaa.avi')
	       
('E:\\1\\b\\aaa', '.avi')
>>> 
