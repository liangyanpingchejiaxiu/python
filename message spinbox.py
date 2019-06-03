from tkinter import *


root = Tk()

w1 =Message(root,text='这是一则消息')
w1.pack()


w2 =Message(root,text='这是一则常常常常消息')# message 自动换行 跟text一样
w2.pack()




w3 =Spinbox(root,from_=0,to=10)
w3.pack()

w4 =Spinbox(root,values=("鸭子","鸡儿","山羊"))
w4.pack()

def create():
    top = Toplevel()        #窗口里面弹出窗口
    top.title("第二个窗口")

    msg = Message(top,text="哒哒哒哒哒") #这里是text
    msg.pack()



b = Button(root,text="创建顶级窗口",command=create)
b.pack()

mainloop()
