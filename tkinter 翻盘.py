from tkinter import *

root = Tk()

a =IntVar()
b =IntVar()#定义整型变量 用户动就变 按钮的状态
c =IntVar()

c1 = Checkbutton(root,text='第一位',variable=a)#这里的variable也就是打勾的框
c1.pack(side=LEFT)
c2 = Checkbutton(root,text='第二位',variable=b)
c2.pack()
c3 = Checkbutton(root,text='第三位',variable=c)
c3.pack(side=RIGHT)

f1 = Label(root,textvariable=a)
f1.pack(side=LEFT)

f2 =Label(root,textvariable=b)
f2.pack()

f3 =Label(root,textvariable=c)
f3.pack(side=RIGHT)

root.mainloop()
