from tkinter import *

window = Tk()

l1 = Listbox(window,selectmode=MULTIPLE)
l1.pack()

for item in ['1','2','3','4','5']:
    l1.insert(END,item) #end表示所有 从0开始




b1 = Button(window,text='删除选中的数字',command=lambda x=l1:x.delete(ACTIVE)) # active相当于end 当前选中的值

b1.pack()
window.mainloop()
    
