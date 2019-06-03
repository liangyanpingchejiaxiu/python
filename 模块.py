Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #模块就是程序
>>> #再源文件夹建立一个py文件 再import文件 就行了
>>> import temperture as t
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import temperture as t
ModuleNotFoundError: No module named 'temperture'
>>> #模块作用 封装组装代码
>>> if __name__=="__main__":
	执行

	
Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    执行
NameError: name '执行' is not defined
>>> #只有再主程序再执行下面的
>>> import sys
>>> sys.path 
['', 'F:\\桌面文件\\Lib\\idlelib', 'F:\\桌面文件\\python37.zip', 'F:\\桌面文件\\DLLs', 'F:\\桌面文件\\lib', 'F:\\桌面文件', 'F:\\桌面文件\\lib\\site-packages']
>>> #加模块搜索路径 sys.path.append("C:\\   ")
>>> #import 包名.文件名
>>> #  from timeit import *

