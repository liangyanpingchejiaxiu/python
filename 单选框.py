#Radiobutton(root,text,variable,value) Radiobutton(root,text,variable,value) 几个 如果value一样就会一起被选 variable要相同
from tkinter import *

root = Tk()

v = IntVar()

group =LabelFrame(root,text='最好的游戏是',padx=5,pady=5)
group.pack(padx=10,pady=10)

games = [('dnf',1),('cf',2),('lol',3)]

for game,num  in games:
    B = Radiobutton(group,text=game,value=num)#单选框中 value不能一样 相同就都勾选了
    B.pack(anchor=W)



root.mainloop()    
