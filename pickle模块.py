Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> my_list=[123,1,2,3'liang',['asas']]
SyntaxError: invalid syntax
>>> my_list=[121331,2121,'sasa']
>>> pickle_file = open('my_list.pkl','wb')
>>> #打开了就一定要关闭
>>> pickle.dump(my_list,pickle_file)
>>> pickle_file.close()
>>> #存成二进制的格式
>>> # b 是二进制打开
>>> pickle_file=open('my_list.pkl','r')
>>> my_list2=pickle.load(pickle_file)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_list2=pickle.load(pickle_file)
UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 0: illegal multibyte sequence
>>> pickle_file=open('my_list.pkl','rb')
>>> my_list2=pickle.load(pickle_file)
>>> print(my_list2)
[121331, 2121, 'sasa']
>>> #可以先把数据存储进去所有都可以 数组元组 更放。方便简洁拿出来用
