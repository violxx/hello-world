#coding=utf-8


import Tkinter as tk
window = tk.Tk()
Label=tk.Label(window,text='please answer my question! \n')
window.geometry('300x300')
window.title('什么鬼')



def firsthand():
    button1.config(text='success!')
button1=tk.Button(window,text='submit',command=firsthand)

Label.pack()
button1.pack()


window.mainloop()
