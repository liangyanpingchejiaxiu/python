Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #描述符
>>> class My:
	def __get__(self,instance,owner):
		print('getting',self,instance,owner)
	def __set__(self,instance,value):
		print(self,instance,value):
			
SyntaxError: invalid syntax
>>> class My:
	def __get__(self,instance,owner):
		print('getting',self,instance,owner)
	def __set__(self,instance,value):
		print('setting',self,instance,value)
	def __delete__(self,instance):
		print('deleting',self,instance)
	#这就是特殊类型的类 My	下面就是它的实例

	
>>> class Test:
	x=My()
	#把特殊类型的类的实例指派给另一个类的属性 这就是描述符 My就是x的描述符 prperty就是一个描述符

	
>>> test=Test()
>>> test.x
getting <__main__.My object at 0x02DB8850> <__main__.Test object at 0x0334A890> <class '__main__.Test'>
>>> #insance就相当于test实例 owner就是Test类本身
>>> test.x='x-man'
setting <__main__.My object at 0x02DB8850> <__main__.Test object at 0x0334A890> x-man
>>> class She:
    def __init__(self,value=28):
        self.value=float(value)
    def __get__(self,instance,owner):
        return  self.value
    def __set__(self,instance,value):
        self.value=float(value)

        
>>> class Hua:
    def __get__(self,instance,owner):
        return instance.she*1.8+32
    def __set__(self,instance,value):
        instance.she=(float(value)-32)/1.8
        #instance就是温度的实例对象 she和hua都是属性

        
>>> class Temperature:
    she=She()
    hua=Hua()

    
>>> temp=Temperature()
>>> temp.she=32
>>> temp.hua
89.6
>>> temp.hua=100
>>> temp.she
37.77777777777778
>>> 
