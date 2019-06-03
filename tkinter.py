from tkinter import *



root = Tk()
textLabel = Label(root,text='有一天\n我看了四十四次日落',justify=LEFT,padx=10)     #左对齐，并且还有一定的距离
textLabel.pack(side=LEFT)
photo = PhotoImage(file='F:\桌面文件\111.gif')                        #创建一个图象Label对象，用PhotoImage实例化一个图片对象
photoLabel = Label(root,image=photo)
photoLabel.pack(side=RIGHT)
mainloop()
