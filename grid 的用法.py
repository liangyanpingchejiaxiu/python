from tkinter import *


root =Tk()




Label(root,text="登录名").grid(row=0,column=0,sticky=W)#sticky 为靠近哪边的  东西南北

Label(root,text="密码").grid(row=1,column=0,sticky=W) #pady是距离上一个的纵向距离


photo=PhotoImage(file = r"C:\Users\Shinelon\Desktop\2.gif")



Label(root,image=photo).grid(row=0,column=3,rowspan=3,pady=5,padx=5)



Entry(root).grid(row=0,column=1)

Entry(root,show="*").grid(row=1,column=1)

Button(root,text="提交",width=5).grid(pady=5,columnspan=3,row=2)
















mainloop()
