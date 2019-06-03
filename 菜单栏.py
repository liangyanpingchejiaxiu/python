from tkinter import *


root =Tk()

def callhello():
    print('你好')


menu1 = Menu(root)

filemenu =Menu(menu1,tearoff=False)
filemenu.add_command(label="打开",command=callhello)
filemenu.add_command(label="保存",command=callhello)
filemenu.add_separator()
filemenu.add_command(label="退出",command=root.quit)
menu1.add_cascade(label="文件",menu=filemenu)


editmenu =Menu(menu1,tearoff=False)
editmenu.add_command(label="复制",command=callhello)
editmenu.add_command(label="粘贴",command=callhello)
editmenu.add_separator()
editmenu.add_command(label="退出",command=root.quit)
menu1.add_cascade(label="文件",menu=filemenu)

root.config(menu=menu1)

mainloop()
