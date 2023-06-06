from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
# root.iconbitmap('')
root.geometry('600x800')

def important_inquiry():
    global lettuce
    lettuce = Label(root,text=var.get()).pack()

var = StringVar()

check_it = Checkbutton(root, text="With lettuce?", variable=var, onvalue="yes please!", offvalue="oh god no again")
check_it.pack()

btn = Button(root, text="let'see...", command=important_inquiry).pack()

root.mainloop()