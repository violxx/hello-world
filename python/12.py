#coding=utf-8


import Tkinter as tk
window = tk.Tk()
window.geometry('300x300')
window.title('什么鬼')
entry1=tk.Entry(window) #定义文本框
entry2=tk.Entry(window)
entry1.pack() #悬挂文本框到窗口
entry2.pack()

def firsthand():
    button1.config(text='success!')
def secondhand():
    button2.config(text='fail!')
button1=tk.Button(window,text='submit',command=firsthand) #定义按钮
button2=tk.Button(window,text='cancle',command=secondhand)
button1.pack()
button2.pack()



window.mainloop()
