from tkinter import Tk, mainloop

from tkinter import *
root = Tk()
root.title("Signature Anzs")
Label(root, text="姓名：", fg="red").grid()
nameent = Entry(root)#, textvariable=StringVar()).grid()
nameent.grid(row=0,column=1)
button = Button(root, text="设置签名", width= "15",height = "2")
button.grid(row=1,column=0)
mainloop()