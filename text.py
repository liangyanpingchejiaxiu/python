from tkinter import *
import webbrowser
root = Tk()

text = Text(root,width=30,height=30)
text.pack()




#photo = PhotoImage(file='f:\2.gif')
text.insert(INSERT,"12345")
text.insert(END,"百度网址")

#def show():
    #text.image_create(END,image=photo)
          

#b = Button(text,text="点我点我",command=show)#插入对象 可以改 text.window_create  image_create
#text.window_create(INSERT,window=b)
text.tag_add("tag1","1.0","1.2","1.4") #tag 从第一行开始 第0列开始 新标签会覆盖旧标签
text.tag_config("tag1",background="green")


text.tag_add("tag2","1.5","1.8")
text.tag_config("tag2",background="yellow",underline=True)
def show_arrow_cursor(event):
    text.config(cursor="arrow")
def show_xterm_cursor(event):
    text.config(cursor="xterm")
def click(event):
    webbrowser.open("www.baidu.com")

    
text.tag_bind("tag2","<Enter>",show_arrow_cursor) #鼠标在上面 不在上面 点击
text.tag_bind("tag2","<Leave>",show_xterm_cursor)
text.tag_bind("tag2","<Button -1>",click) #要导入webbrowser模块

#检查  contents =text.get("1.0",END)
# def getsig(contents):
   #  m=hashlib,md5(contents.encode())
   #  return m.digest() 要导入 hashlib 模块
#sig =getsig(contents)
#def check():
#   contents = text.get("1.0",END)
#   if sig !=getsig(contents):
#       print("警报")
#   else:
#       print("风平浪静")
#Button(root,text="检查",command=check).pack()

mainloop()

