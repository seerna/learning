from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('')
# root.iconbitmap('')

def open_a_file():
    root.filename = filedialog.askopenfilename(
        initialdir="~/Documents/Learning \Code/tkinter/freeCodeCamp_tutorial/images/",
        title="Pick a file", filetypes=(
            ("jpg files", "*.jpg"),
            ("jpeg files","*.jpeg"),
            ("all files","*.*"),
            ),
        )
    global a_label, an_image, a_label_image
    a_label = Label(root, text=root.filename).pack()
    an_image = ImageTk.PhotoImage(Image.open(root.filename))
    a_label_image = Label(root, image=an_image).pack()

btn = Button(root, text="Select a file", command=open_a_file).pack()

root.mainloop()