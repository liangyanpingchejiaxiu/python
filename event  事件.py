from tkinter import *

root = Tk()
def callback(event):
    print("点击位置:",event.x,event.y)#event是对于程序来说的  root是对于整个idle来说



frame= Frame(root,width=200,height=200)
frame.bind("<Button-1>",callback) #-1 左键 2 中间 3 右键
frame.pack()

def callback1(event):
              print(event.char) #event相当于 事件中的值



frame1= Frame(root,width=200,height=200)
frame1.bind("<Key>",callback1) #<Motion> 就是鼠标移动的地方
frame1.focus_set()
frame1.pack()



#KeyPress -h 按住h时 shif-alt-KeyPress-a  三个一起按









mainloop()
