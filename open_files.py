from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('')
# root.iconbitmap('')

root.filename = filedialog.askopenfilename(
    initialdir="~/Documents/Learning \code/Python/tkinter/freeCodeCamp_tutorial/images/",
    title="Pick a file", filetypes=(("jpg files", "*.png"),("jpeg files","*.jpeg"),("all files","*.*")
    )
)
root.mainloop()