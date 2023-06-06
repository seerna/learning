from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('')
# root.iconbitmap('')
root.geometry('600x800')

def clicked():
    global selection
    selection = Label(root, text=dropdown.get()).pack()

options = [
    'prick this',
    'Not! Tis',
    'Oh yeah here',
    'keep it',
    'add stuff'
    ]

dropdown = StringVar()
dropdown.set(options[0])

# Note the *, it's done so options is taken as items and not an entire list
omg_drop = OptionMenu(root, dropdown, *options)
omg_drop.pack()

btn = Button(root, text='select', command=clicked).pack()

root.mainloop()